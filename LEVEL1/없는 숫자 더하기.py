## 없는 숫자 더하기 - 프로그래머스 월간 코드 챌린지 시즌3  
## https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = 0
    num_list = [0,1,2,3,4,5,6,7,8,9]
    my_list = []
    for number in numbers:
        my_list.append(number)
    answer = sum((list(set(num_list) - set(my_list))))
    return answer
    
