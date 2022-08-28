## 소수 만들기 - Summer/Winter Coding(~2018)
## https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
import math
def solution(nums):
    answer = -1
    num_list = []
    # 서로 다른 3개 숫자 : Combinations
    coms = list(combinations(nums,3))
    
    for com in coms:
        temp = com[0] + com[1] + com[2]
        # 소수 판별
        flag = False
        for i in range(2,int(math.sqrt(temp)) + 1):
            if temp % i == 0:
                flag = True
        # 소수일 경우 append
        if flag == False:
            num_list.append(temp)

    return len(num_list)
  
  
