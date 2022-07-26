## 신규 아이디 추천 - 2021 KAKAO BLIND RECRUITMENT 
## https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    for alpha in new_id:
        if alpha.isalnum() or alpha in '-_.':
            answer += alpha
    #3
    while '..' in answer:
        answer = answer.replace('..','.')
    #4
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 1 and answer[-1] == '.':
        answer = answer[:-1]
    #5
    if len(answer) == 0:
        answer = 'a'
    #6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
  
