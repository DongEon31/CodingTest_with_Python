## 실패율 - 2019 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    users = {k+1:0 for k in range(N+1)}
    fail = {k+1:0 for k in range(N)}
    total_users = len(stages)
    
    for stage in stages: # 각 stage별 막힌 구간의 유저 수 저장
        users[stage] += 1
        
    user_count = total_users # 전체 유저수
    for i in range(N):
        if user_count != 0: ##### 도달한 유저가 있어야 하므로 조건 추가
            fail[i+1] = (users[i+1]/user_count) # 해당 스테이지에서 막힌 유저 수 / 도달한 유저 수
        else: fail[i+1] = 0 ##### 도달한 유저가 없으면 0/0 대신 확률 0으로 처리;
        user_count -= users[i+1] # [i+1] 스테이지에 도달한 유저수
        
    des = sorted(fail.items(),key = lambda x:x[1],reverse=True) # 실패율 기준으로 내림차순 정렬
    for d in des:
        answer.append(d[0])
    return answer
  
  
