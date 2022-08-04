## 가운데 글자 가져오기
## https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    if len(s)%2==1: # 홀수 case
        mid = len(s)//2
        answer += s[mid]
    else: # 짝수 case
        mid1 = int(len(s)/2) - 1
        mid2 = mid1 + 1
        answer = answer + s[mid1] + s[mid2]
    return answer
  
  
