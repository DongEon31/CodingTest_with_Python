## 로또의 최고 순위와 최저 순위 - 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
## https://school.programmers.co.kr/learn/courses/30/lessons/77484#fnref1

def solution(lottos, win_nums):
    answer = []
    right = 0
    erased = 0
    for lotto in lottos:
        if lotto in win_nums:
            right += 1
        elif lotto == 0:
            erased += 1
    
    if right + erased == 6:
        answer.append(1)
    elif right + erased == 5:
        answer.append(2)
    elif right + erased == 4:
        answer.append(3)
    elif right + erased == 3:
        answer.append(4)
    elif right + erased == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if right == 6:
        answer.append(1)
    elif right == 5:
        answer.append(2)
    elif right == 4:
        answer.append(3)
    elif right == 3:
        answer.append(4)
    elif right == 2:
        answer.append(5)
    else:
        answer.append(6)
        
        
        
        
        
    return answer
  
  
