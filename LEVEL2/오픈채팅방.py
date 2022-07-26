## 오픈채팅방 - 2019 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict
def solution(record):
    # 어떤 uid가 들어왔는지 / 나갔는지를 기록하고, 최종 uid의 닉네임이 뭔지만 잘 알면 된다.
    answer = []
    chat = []
    nickname = defaultdict()
    for rec in record:
        data = rec.split()
        if data[0] == 'Enter':
            chat.append(['들어왔습니다',data[1]]) # 0 : Enter
            nickname[data[1]] = data[2] # data[1] = uid(key), data[2] = nickname(val)
        elif data[0] == 'Leave':
            chat.append(['나갔습니다',data[1]]) # 1 : Leave
        else : # Change
            nickname[data[1]] = data[2]                 
    for i in range(len(chat)):
        answer.append("{nick}님이 {state}.".format(nick = nickname[chat[i][1]], state = chat[i][0]))
    return answer
 
