## 하샤드 수
## https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    origin, length = x, len(str(x))
    remain = 0
    # 10으로 나누면서 각 자릿수 더하기
    for i in range(length):
        remain += x % 10
        x -= x % 10
        x //= 10
        
    answer = True if origin % remain == 0 else False
    return answer
  
  
