## 같은 숫자는 싫어
## https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    answer = []
    for num in arr:
        if len(answer)>0 and num == answer[-1]:
            continue
        else:
            answer.append(num)
    return answer
  
