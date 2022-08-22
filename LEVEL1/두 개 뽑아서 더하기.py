## 두 개 뽑아서 더하기 - 월간 코드 챌린지 시즌1
## https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(numbers):
    answer = []
    two_list = list(combinations(numbers,2))
    for two in two_list:
        answer.append(two[0]+two[1])
    answer = sorted(list(set(answer)))
    return answer
  
  
