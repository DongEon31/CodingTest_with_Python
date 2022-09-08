## 네트워크
## https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import defaultdict, deque
def solution(n, computers): # 0 ~ n-1
    answer = 0
    network = defaultdict(list)
    visited = [False] * n
    # network 만들기 - i==j인 경우는 제외
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                network[i].append(j)
    net = deque()
    visited[0] = True
    # 모든 점에 대해 Search
    for start in range(n):
        if start != 0 and visited[start] == True: # 이미 방문한 점은 pass
            continue
        elif start == 0 or visited[start] == False: # 0이거나 방문한 적 없으면 BFS
            net.append(start)
            while net:
                now = net.popleft()
                for node in network[now]:
                    if visited[node] == False:
                        net.append(node)
                        visited[node] = True
            answer += 1
    return answer
  
  
