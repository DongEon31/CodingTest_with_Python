## 크레인 인형뽑기 게임 - 2019 카카오 개발자 겨울 인턴십
## https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0    
    basket = [] 
    for m in moves:
        for row in board: # 맨 위에서부터 탐색
            if row[m-1] == 0 : # 인형이 없는 경우
                continue # pass로 해도 런타임은 비슷하다.
            else : # 인형이 있는 경우
                basket.append(row[m-1])
                row[m-1] = 0 # 빈 공간 만들기.
                break # m에 대한 뽑기 종료.
                
        # 뽑은 직후, basket 내 두 인형이 같은지 check
        # basket에 인형이 하나만 있는 경우, '==' 연산에서 index error 발생 : 길이 check
        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket = basket[:-2]
            answer += 2
    return answer
  
