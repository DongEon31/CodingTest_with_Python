## 예상 대진표 - 2017 팁스타운
## https://school.programmers.co.kr/learn/courses/30/lessons/12985

import math
def solution(n,a,b):
    answer = 0
    count = 1
    while True:
        if abs(a - b) == 1: # a와 b와 1 차이 CHECK.
            if a > b and a%2==0 and b%2==1: 
                return count
            elif a < b and a%2==1 and b%2==0: 
                return count   
        # 다음 대진으로.       
        a = math.ceil(a/2) 
        b = math.ceil(b/2)
        count += 1
        
