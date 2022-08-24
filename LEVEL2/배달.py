## 배달- Summer/Winter Coding(~2018)
## https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq
def solution(N, road, K):
    answer = 0
    INF = 987654321
    town = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    for data in road: # data[0] : start / data[1] : end / data[2] : dist
        town[data[0]].append((data[2],data[1]))
        town[data[1]].append((data[2],data[0]))
    
    q = [] # heapq 생성
    heapq.heappush(q,(0,1)) # 시작 지점 push
    distance[1]=0 # 시작 지점의 길이는 0
    while q:
        dist, node = heapq.heappop(q) 
        if distance[node] < dist: # distance 리스트보다 길면 무시
            continue
        for d, n in town[node]:
            if dist + d < distance[n]: # 최단 거리 갱신
                distance[n] = dist + d
                heapq.heappush(q,(dist + d,n)) # 갱신된 길이를 push. 가장 작은 값은 heapq의 맨 앞으로 옴
    
    return len([final for final in distance if final <= K])
  
  
