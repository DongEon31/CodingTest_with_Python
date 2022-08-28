## 두 정수 사이의 합
## https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if a == b:
        return a
    m, n = max(a,b), min(a,b)
       
    return (m-n+1)*n + ((m-n)**2 + (m-n)) // 2
  
  
