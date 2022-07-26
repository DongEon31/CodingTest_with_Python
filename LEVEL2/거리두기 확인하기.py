## 거리두기 확인하기 - 2021 카카오 채용연계형 인턴십
## https://school.programmers.co.kr/learn/courses/30/lessons/81302#fn1

from collections import deque
def bfs(place):
    person = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                person.append((i,j))
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for start in person:
        queue = deque([start])
        visited = [[0 for _ in range(5)] for _ in range(5)] # 방문 여부 CHECK
        distance = [[0 for _ in range(5)] for _ in range(5)] # 실시간 거리를 담는 LIST
        visited[start[0]][start[1]] = 1
        while queue:
            x,y = queue.popleft()
            for z in range(4): # 상,하,좌,우 CHECK
                nx = x + dx[z]
                ny = y + dy[z]
                # 배열 내 만족 + 방문 아직 안 한 곳 
                if nx >= 0 and ny >= 0 and nx < 5 and ny < 5 and visited[nx][ny] == 0: 
                    # Table 'O' : 빈 공간이므로 계속 진행.
                    if place[nx][ny] == 'O':
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                    # Person 'P' : 거리가 2 이하면 거리두기 걸린 것. return 0
                    elif place[nx][ny] == 'P' and distance[x][y] < 2:
                        return 0
                    # Partition 'X' : 아예 가지도 못하므로 알아서 처리됨.
    # 모든 start에 대해 문제 없으면 거리두기 잘 된것. return 1
    return 1              

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer
