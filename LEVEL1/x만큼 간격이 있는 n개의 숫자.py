## x만큼 간격이 있는 n개의 숫자
## https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer
