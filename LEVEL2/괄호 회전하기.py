## 괄호 회전하기 - 월간 코드 챌린지 시즌2
## https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    gwalho_list = ['(','[','{']
    pair = {')':'(', ']':'[', '}':'{'}
    
    for i in range(len(s)):   
        stack = []
        flag = True
        temp = s[0]
        s = s[1:] + temp # 왼쪽으로 밀기
        for alpha in s:
            if alpha in gwalho_list: # ([{
                stack.append(alpha) # push
            else: # )]}
                # stack의 top과 쌍이 맞아야 함
                if len(stack) > 0 and stack[-1] == pair[alpha]: 
                    stack.pop()  # pop
                # 쌍이 맞지 않거나, stack이 없는데 닫는 괄호가 오면 틀린 문자열임
                else:  
                    flag = False
        # s를 다 돌았는데 stack이 비었으면, 올바른 문자열임
        if len(stack) == 0 and flag == True:
            answer += 1
                    
    return answer
  
  
