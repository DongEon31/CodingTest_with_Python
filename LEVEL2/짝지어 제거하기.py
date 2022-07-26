## 짝지어 제거하기 - 2017 팁스타운 
## https://school.programmers.co.kr/learn/courses/30/lessons/12973

from collections import deque
def solution(s):
    answer = -1
    new_s = deque() # Stack
    for alpha in s:
        new_s.append(alpha)
        while len(new_s) > 1 and new_s[-1] == new_s[-2]:
            new_s.pop()
            new_s.pop()
    if len(new_s) == 0 : answer = 1
    else : answer = 0
    return answer
  
