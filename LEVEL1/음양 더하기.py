## 음양 더하기 - 월간 코드 챌린지 시즌2
## https://school.programmers.co.kr/learn/courses/30/lessons/76501
 
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True : t = 1
        else : t = -1
        absolutes[i] *= t
        answer +=  absolutes[i]
    return answer
  
