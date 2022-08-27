## 서울에서 김서방 찾기
## https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    answer = ''
    for idx, name in enumerate(seoul):
        if name == 'Kim':
            answer = '김서방은 ' + str(idx) + '에 있다'
    
    return answer
    
    
