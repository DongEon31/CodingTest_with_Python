## 게임 맵 최단거리
## https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
def solution(maps):
    INF = 987654321
    answer = 0
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dist = [[INF for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque()
    q.append((0,0))
    
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    dist[0][0] = 1
    while q:
        x, y = q.popleft()     
#       visited[dy][dx] = True
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            # 길이면 push.
            if 0 <= dx < len(maps[0]) and 0 <= dy < len(maps) and maps[dy][dx] == 1 and visited[dy][dx] == False:
                q.append((dx,dy))
                visited[dy][dx] = True
                # 해당 경로가 더 짧으면 갱신, 길면 pass
                if dist[dy][dx] > dist[y][x] + 1:
                    dist[dy][dx] = dist[y][x] + 1
                
    if dist[-1][-1] == INF:
        return -1
    else:
        return dist[-1][-1]
        
        
