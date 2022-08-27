## 나누어 떨어지는 숫자 배열
## https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num) 
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer
  
  
