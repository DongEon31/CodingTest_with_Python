## 문자열 압축 - 2020 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 987654321
    for i in range(1,len(s)//2 + 2): # len(s) == 1인 경우를 대비, +1 대신 +2
        pattern = s[:i]
        new_s = ''
        count = 1
        for split in range(i,len(s)+1,i):
            if pattern == s[split:split+i]: # pattern과 같은 단어를 만났다면
                count += 1
            else: # 다를 때
                if count == 1: # 1회 반복되면 숫자 X
                    new_s += pattern
                else: # 2회 이상 반복되면 숫자 포함
                    new_s = new_s + str(count) + pattern
                # count, pattern 초기화
                count = 1
                pattern = s[split:split+i]
        answer = min(answer, len(new_s)+len(s) % i)
    return answer
  
  
