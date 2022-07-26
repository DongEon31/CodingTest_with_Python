## 부족한 금액 계산하기 - 위클리 챌린지 
## https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1
    total = 0
    for n in range(count):
        new_price = price * (n+1)
        total += new_price
    if total > money :
        answer = total - money
    else :
        answer = 0
    
    return answer
  
