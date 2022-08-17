## JadenCase 문자열 만들기
## https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    # 각 단어의 첫 알파벳만 check하고, 이후 단어들은 lower 처리.
    for idx, alpha in enumerate(s):
        if idx == 0 or s[idx-1] == ' ': # 첫 글자인지 check
            if alpha.isalpha() and alpha.islower(): # 소문자 알파벳이라면 대문자로 추가!
                answer += alpha.upper()
            else: # 숫자이거나 대문자라면 그대로 추가!
                answer += alpha
        else: # 첫 글자가 아니라면 소문자로 추가!
            answer += alpha.lower()
                
    return answer
  
  
