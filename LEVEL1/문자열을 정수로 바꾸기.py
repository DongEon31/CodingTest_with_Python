## 문자열을 정수로 바꾸기
## https://school.programmers.co.kr/learn/courses/30/lessons/12925 

def solution(s):
    answer = 0
    if s[0] == '+':
        return int(s[1:])
    else:
        return int(s)
    
    return answer
   
