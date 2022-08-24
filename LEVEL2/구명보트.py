## 구명보트 - 탐욕법(Greedy)
## https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque
def solution(people, limit):
    answer = 0
    d = deque(sorted(people))
    
    while d:
        if len(d) == 1: # 한 명 남은 경우
            d.pop()
        elif d[0] + d[-1] <= limit: # 최대, 최소를 한 보트에 태우는 경우
            d.pop()
            d.popleft()
        elif d[-1] + d[-2] <= limit: # 가장 작은 두 명을 한 보트에 태우는 경우
            d.pop()
            d.pop()
        else: # 한 명밖에 못 타는 경우
            d.pop()
        answer += 1
    return answer
