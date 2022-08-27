## 정수 내림차순으로 배치하기
## https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = ''
    str_n = str(n)
    new_n = []
    
    for i in range(len(str_n)):
        new_n.append(n%10)
        n -= n%10
        n //= 10
        
    new_n.sort(reverse=True)
    
    for i in range(len(str_n)):
        answer += str(new_n[i])
                   
    return int(answer)

