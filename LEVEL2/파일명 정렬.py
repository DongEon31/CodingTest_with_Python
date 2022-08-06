## 파일명 정렬 - 2018 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/17686 

def solution(files):
    answer = []    
    new_files = []  # 내부의 각 파일에 ['원본', HEAD, NUMBER]로 구분하여 저장. TAIL은 사용되지 않으니 버림
    # new_files 리스트 만들기
    for file in files:
        origin = file
        HEAD, NUMBER = '', ''
        
        # HEAD
        for alpha in file:
            if alpha.isdigit():
                break
            else:
                HEAD += alpha
        # file 자르기        
        file = file[len(HEAD):]
        
        # NUMBER
        idx = 0
        for alpha in file:
            if idx < 5 and alpha.isdigit():
                NUMBER += alpha
                idx += 1
            else:
                break
        new_files.append([origin, HEAD.lower(), int(NUMBER)]) # 대소문자 구분 X, lstrip('0')으로 앞의 0 제거
        
    # HEAD 먼저, 다음 NUMBER 기준 정렬
    SORTED = sorted(new_files, key = lambda x : (x[1], x[2]))
    
    for name in SORTED:
        answer.append(name[0])
    return answer

