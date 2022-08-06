## 문자열 내 p와 y의 개수
## https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False
      
      
