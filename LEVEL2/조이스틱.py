## 조이스틱
## https://school.programmers.co.kr/learn/courses/30/lessons/42860#

from collections import deque
def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    # 위아래 조작
    for idx, alpha in enumerate(name):
        if ord(alpha) - ord('A') < ord('Z') - ord(alpha) + 1 : # 다음 알파벳
            answer += ord(alpha) - ord('A')
        else: # 이전 알파벳
            answer += ord('Z') - ord(alpha) + 1
        
        # 실시간 좌우 조작
        right = idx + 1
        while right < len(name) and name[right] == 'A':
            right += 1
            
        # 3가지 중 최단 경로를 갱신
        min_move = min([min_move, 2 * idx + len(name) - right, idx + 2 * (len(name) -right)])
        
    answer += min_move
    return answer
   
  
