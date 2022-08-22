## 나머지가 1이 되는 수 찾기 - 월간 코드 챌린지 시즌3 
## https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 0
    number = 2
    while True:
        if n % number == 1:
            return number
        number += 1
        
        
