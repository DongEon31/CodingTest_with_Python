## 2개 이하로 다른 비트 - 월간 코드 챌린지 시즌2
## https://school.programmers.co.kr/learn/courses/30/lessons/77885

def f(x):
    if x%2 == 0 or x == 1: # 짝수
        return x + 1
    else : # 홀수
        last = (~x) & (x+1) 
        return (x|last) & ~(last>>1)   
    
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(number))
    return answer
  
