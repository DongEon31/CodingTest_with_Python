## 2016년
## https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    a_list = [0,31,29,31,30,31,30,31,31,30,31,30]
    day_list = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    answer += day_list[(sum(a_list[0:a]) + b) % 7]
    return answer
  
  
