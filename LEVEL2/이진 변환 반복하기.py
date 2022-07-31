## 이진 변환 반복하기 - 월간 코드 챌린지 시즌1
## https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    # s -> 1이 될 때까지 이진 변환 횟수와 지워진 0의 개수 return
    total_zeros = 0
    bin_count = 0
    while True:
        bin_count += 1 # 이진 변환 횟수
        zero_count = 0 # s 내 0 개수 세기
        for i in range(len(s)):
            if s[i] == '0' :
                zero_count += 1
        total_zeros += zero_count
        if len(s) - zero_count == 1: # s = '1'이면 종료.
            break
        else: # 아니면, 길이를 이진수로 변환
            s = bin(len(s) - zero_count)[2:]
    answer.append(bin_count)
    answer.append(total_zeros)       
    
    return answer
  
  
