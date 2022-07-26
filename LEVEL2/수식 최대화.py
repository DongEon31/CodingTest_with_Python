## 수식 최대화 - 2020 카카오 인턴십 
## https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
def solution(expression):
    operators = ["*", "+", "-"]
    answer = []
    # 모든 연산 우선순위 조합에 대해 반복
    for operator in permutations(operators, 3):
        temp_exp = [""]
        for exp in expression: # operand : 문자열이므로 기존 숫자에 이어붙이기
            if exp.isdigit() and temp_exp[-1] not in operators:
                temp_exp[-1] += exp
            else: # operator OR operand 첫 글자 : 따로 append 
                temp_exp.append(exp)
        for i in operator:
            while i in temp_exp:
                idx = temp_exp.index(i)
                # idx - 1 , idx , idx + 1은 eval() 함수로 계산한 값을 저장,
                # 슬라이싱으로 temp_exp 갱신
                temp_exp = temp_exp[:idx-1]+[str(eval("".join(temp_exp[idx-1:idx+2])))]+temp_exp[idx+2:]
        answer.append(abs(int(temp_exp[0])))
    return max(answer)
  
