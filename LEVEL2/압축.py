## 압축 - 2018 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    alpha_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                 'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    # 스킵할 인덱스 수 count
    count = 0
    # while문에서 즉시 종료하기 위한 flag
    flag = False
    for i, word in enumerate(msg):
        idx = alpha_dict[word]
        if count >0: # count만큼 pass.
            count -= 1
            continue    
        if len(word)==1: # 첫 글자는 무조건 dict에 존재함. 다음 step으로
            idx = alpha_dict[word]
            if i+1 == len(msg): # msg 마지막 글자면 break.
                answer.append(idx)
                break
            i += 1
            word += msg[i]
            while word in alpha_dict.keys(): # 둘 이상 문자열이 dict에 있는 경우 -> dict에 없는 문자를 만날 때까지.
                idx = alpha_dict[word]
                if i+1 == len(msg): # msg 마지막 글자면 break.
                    answer.append(idx)
                    flag = True # 이중 loop이므로 flag를 이용해 즉시 종료
                    break
                i += 1
                word += msg[i]
                count += 1    
        if flag == True:
            break
        # dict에 없는 경우.
        alpha_dict[word] = 27 + len(answer)
        answer.append(idx)
    return answer
  
  
