## 약수의 개수와 덧셈 - 월간 코드 챌린지 시즌2
## https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        count = 0
        for i in range(num):
            if num%(i+1)==0:
                count += 1
        if count % 2 == 0: # 짝수
            answer += num
        else: # 홀수
            answer -= num
    
    return answer
  
 
