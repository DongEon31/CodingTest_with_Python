## 괄호 변환 - 2020 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''
    #1
    if p == answer:
        return answer
    #2
    left, right = 0,0
    for index, i in enumerate(p):
        if i == '(' : left += 1  
        else : right += 1
        if left==right:
            u, v = p[:index+1], p[index+1:]
            break
    #3
    count, correct = 0, True
    for i in u:
        if i == '(' : count += 1  
        else : count -= 1
        if count < 0 : correct = False
    if correct:
        u += solution(v)
        return u
    #4
    else:
        new = '('
        new += solution(v)
        new += ')'
        u = u[1:-1]
        u = u.replace('(','*')
        u = u.replace(')','(')
        u = u.replace('*',')')
        new += u
        return new
      
    
