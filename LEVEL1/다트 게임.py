## 다트 게임 - 2018 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/17682

import re
def solution(dartResult):
    answer = 0
    score=[]
    dartlist = re.split('S|D|T',dartResult)
    
    for alpha in dartResult:
        if alpha.isalpha():
            if alpha == 'S':
                score.append(1)
            elif alpha == 'D':
                score.append(2)
            else:
                score.append(3)

    for idx, dart in enumerate(dartlist):
        if len(dart)>0:
            if dart[0].isdigit(): # bonus 없음
                score[idx] = int(dart) ** score[idx]
            else: # bonus!
                if len(dart)>1 : # bonus + number
                    score[idx] = int(dart[1:]) ** score[idx]
                if dart[0] == '*' : # 해당 score, 이전 score 2배.
                    score[idx-1] *= 2
                    if idx>1:
                        score[idx-2] *= 2
                else: # 해당 score -배.
                    score[idx-1] = -score[idx-1]
                    
    answer = sum(score)                
    return answer
  
 
