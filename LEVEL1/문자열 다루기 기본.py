## 문자열 다루기 기본
## https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True
    answer = True if s.isdigit() and (len(s) == 4 or len(s) == 6) else False
    return answer
  
  
