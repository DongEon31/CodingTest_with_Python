## 경주로 건설 - 2020 카카오 인턴십
## https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    def bfs(start):
        direc = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]} # 북,동,남,서 순서
        length = len(board)
        visited = [[987654321]*length for _ in range(length)]
        visited[0][0] = 0

        q = deque([start]) # x, y, cost, dir
        while q:
            x, y, cost, d = q.popleft()
            for i in range(4): # 북,동,남,서 순서
                nx = x + direc[i][0]
                ny = y + direc[i][1]

                # board 안에 있고, 벽이 아닌지 확인
                if 0 <= nx < length and 0 <= ny < length and board[nx][ny] == 0:
                    
                    # 비용계산
                    if i == d : ncost = cost + 100
                    else : ncost =  cost + 600
                    # 최소 비용이면 갱신 후 endeque!
                    if ncost < visited[nx][ny]:
                        visited[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])
                        
        return visited[-1][-1]
    
    return min([bfs((0, 0, 0, 1)), bfs((0, 0, 0, 2))])
  
  
