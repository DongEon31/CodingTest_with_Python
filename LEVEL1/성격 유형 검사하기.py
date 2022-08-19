## 성격 유형 검사하기 - 2022 KAKAO TECH INTERNSHIP
## https://school.programmers.co.kr/learn/courses/30/lessons/118666
 
def solution(survey, choices):
    answer = ''
    check_dict = {'R' : 0, 'T' : 0, 'F' : 0, 'C' : 0, 'M' : 0, 'J' : 0, 'A' : 0, 'N' : 0 }
    for idx, question in enumerate(survey):
        if choices[idx] == 4: # center
            continue
        elif choices[idx] - 4 < 0: # left
            check_dict[question[0]] += abs(choices[idx] - 4)
        else: # right
            check_dict[question[1]] += abs(choices[idx] - 4)
    
    
    if check_dict['R'] >= check_dict['T']:
        answer += 'R' 
    else:
        answer += 'T'
    if check_dict['C'] >= check_dict['F']:
        answer += 'C' 
    else:
        answer += 'F'
    if check_dict['J'] >= check_dict['M']:
        answer += 'J' 
    else:
        answer += 'M'
    if check_dict['A'] >= check_dict['N']:
        answer += 'A' 
    else:
        answer += 'N'
        
    return answer
  
  
