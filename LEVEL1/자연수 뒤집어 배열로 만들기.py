## 자연수 뒤집어 배열로 만들기
## https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    for i in range(len(str(n))):
        answer.append(int(str(n)[-i-1]))
    
    return answer
  
  
