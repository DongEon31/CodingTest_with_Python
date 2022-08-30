## 자릿수 더하기
## https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=python3

def solution(n):
    answer = 0
    while True:
        answer += n % 10
        if n < 10 : break
        n -= n % 10
        n //= 10
    
    return answer
  
  
