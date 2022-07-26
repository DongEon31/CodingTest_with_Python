## 모의고사 
## https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    order = [0] * 3
    t1 = [1,2,3,4,5] # 1
    t2 = [2,1,2,3,2,4,2,5] # 2
    t3 = [3,3,1,1,2,2,4,4,5,5] # 3

    for i in range(len(answers)):
        if answers[i] == t1[i % len(t1)]: # 1
            order[0] += 1
        if answers[i] == t2[i % len(t2)]: # 2
            order[1] += 1
        if answers[i] == t3[i % len(t3)]: # 3 
            order[2] += 1

    for i in range(len(order)): # 앞 사람부터 최댓값 탐색 : 자동으로 오름차순
        if order[i] == max(order): 
            answer.append(i+1)      

    return answer
