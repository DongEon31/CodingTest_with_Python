## 신고 결과 받기 - 2022 KAKAO BLIND 
## https://school.programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict # 각 index에 값을 미리 할당하지 않아도 된다 !!

def solution(id_list, report, k):
    answer = [0] * len(id_list) # user id수만큼 리스트 생성
    report = set(report) # user1 -> user2에 대한 여러 번의 신고는 하나로 간주. set()를 통해 중복 제거
    reported = defaultdict(int) # key - user id, value - reported counts.
    report_list = defaultdict(list) # key - user id, value - report users.
    ban_list = [] # k회 이상 신고되어 정지된 user list
    
    for r in report: 
        user1, user2 = r.split(' ')
        reported[user2] += 1 # 신고당한 user는 reported 횟수 추가
        report_list[user1].append(user2) # report_list[user1]에 user2를 추가.
        
        if reported[user2] == k: # banned user
            ban_list.append(user2)
    
    for b in ban_list: # ban list check
        for i in range(len(id_list)): # 모든 user를 check
            if b in report_list[id_list[i]]: # ban user가 report_list에 있으면 Mail.
                answer[i] += 1
    return answer
  
