## 콜라츠 추측
## https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    
    # 입력 1 예외처리
    if num == 1 : return 0

    # 1이 될 때까지 반복
    for i in range(500):
        num = num//2 if num % 2 == 0 else (num * 3) + 1
        answer += 1
        if num == 1 :
            break
    
    # 500번 후에도 1이 아니면 -1을 return
    if num != 1 : return -1
    return answer
  
  
