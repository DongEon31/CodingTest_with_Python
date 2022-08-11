## 올바른 괄호
## https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    gwalho_list = []
    for gwalho in s:
        if gwalho == '(':
            gwalho_list.append(gwalho)
        elif gwalho == ')' and len(gwalho_list) > 0:
            gwalho_list.pop()
        else:
            return False
    
    if len(gwalho_list) > 0:
        return False
    
    return True
   
   
