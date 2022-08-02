## 시저 암호
## https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha.isalpha():
            if alpha.islower(): # a 기준, alpha와의 차이 + n만큼 플러스
                answer += chr(ord('a') + (ord(alpha) - ord('a') + n)%26)
            else: # A 기준, alpha와의 차이 + n만큼 플러스
                answer += chr(ord('A') + (ord(alpha) - ord('A') + n)%26)
        else:
            answer += ' '
    return answer
    
