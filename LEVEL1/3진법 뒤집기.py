## 3진법 뒤집기 - 월간 코드 챌린지 시즌1
## https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    new_n = ''
    s=0
    
    # 3진법 자릿수 구하기. 등호 포함 
    while n >= 3**(s+1):
        s += 1
    
    # 윗자리부터 0,1,2 채우기
    while n != 0:
        new_n += str(n//(3**s))
        n -= (n//(3**s))*(3**s)
        s -= 1
    
    # 역순 슬라이싱
    new_n = new_n[::-1]
    
    # STRING 형의 n진수를 10진수로 : int(STRING,n)
    answer = int(new_n,3)
    return answer
  
 
