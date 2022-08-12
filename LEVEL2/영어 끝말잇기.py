## 영어 끝말잇기 - Summer/Winter Coding(~2018)
## https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    temp = []
    for word in words:
        if len(temp) == 0: # 시작 단어
            temp.append(word)
        elif temp[-1][-1] == word[0] and word not in temp: # 이어지고 중복이 아니라면 pass
            temp.append(word)
        else: # wrong
            order = len(temp) + 1
            return [n if order % n == 0 else order % n,((order - 1) // n) + 1]
    
    return [0,0]
  
  
