## 프렌즈4블록 - 2018 KAKAO BLIND RECRUITMENT 
## https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        pop_list = board.pop(0)
        board.append([p for p in pop_list])
        
    while True:
        where_is_22 = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '0':
                    continue
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    where_is_22.append((i,j))
                    where_is_22.append((i,j+1))
                    where_is_22.append((i+1,j))
                    where_is_22.append((i+1,j+1))
        # 더 이상 터질 게 없으면 while 탈출.
        if len(where_is_22) == 0 :
            break
        else:
            answer += len(set(where_is_22))   
            # 2*2 => Bomb
            for c in where_is_22:
                board[c[0]][c[1]] = '0'
            # 뒤에서부터 
            for c in reversed(where_is_22):   
                check = c[0] - 1
                put = c[0]
                
                while check >= 0:       
                    if board[put][c[1]] == "0" and board[check][c[1]] != "0":
                        board[put][c[1]] = board[check][c[1]]
                        board[check][c[1]] = "0"
                        put -= 1
                    check -= 1

    return answer
  
