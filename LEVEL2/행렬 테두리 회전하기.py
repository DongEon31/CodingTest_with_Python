## 행렬 테두리 회전하기 - 2021 Dev-Matching: 웹 백엔드 개발자
## https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    board = [[columns * j + i + 1 for i in range(columns)] for j in range(rows)]
    
    for query in queries:
        top = query[0] - 1 # top
        left = query[1] - 1 # left
        bottom = query[2] - 1 # bottom
        right = query[3] - 1 # right
        temp = board[top][left] # 왼쪽 위
        minimum = temp # 매번 밀면서 최솟값 check
        for a in range(bottom - top): # 왼쪽 모서리 올리기
            board[top + a][left] = board[top + a + 1][left]
            minimum = min(minimum,board[top + a + 1][left])
            
        for b in range(right - left): # 아래 모서리 오른쪽 밀기
            board[bottom][left + b] = board[bottom][left + b + 1]
            minimum = min(minimum,board[bottom][left + b + 1])
            
        for c in range(bottom - top): # 오른쪽 모서리 내리기
            board[bottom - c][right] = board[bottom - c - 1][right]
            minimum = min(minimum, board[bottom - c - 1][right])
            
        for d in range(right - left): # 위 모서리 왼쪽 밀기
            board[top][right - d] = board[top][right - d - 1]
            minimum = min(minimum, board[top][right - d - 1])
        board[top][left + 1] = temp
        answer.append(minimum)
    return answer
  
  
