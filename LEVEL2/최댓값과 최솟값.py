## 최댓값과 최솟값.py
## https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    nums = s.split(' ')
    my_max, my_min = '-987654321', '987654321'
    for num in nums:
        if int(num) < int(my_min):
            my_min = num
        if int(num) > int(my_max):
            my_max = num
    answer += my_min + ' ' + my_max        
    return answer
    
