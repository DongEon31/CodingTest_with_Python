## 카펫 - 탐색
## https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    xy=brown+yellow # 넓이
    num=3
    while xy//num >= 3: # yellow가 존재하려면 한 변의 길이가 3 이상
        if xy%num==0 and (xy//num - 2)*(num - 2) == yellow: # 넓이 조건 + yellow 조건 만족 => answer
            temp = xy//num
            if temp > xy//temp: # x가 더 크게
                x = temp
                y = xy//temp
                break
            else:
                y = temp
                x = xy//temp
                break
        num += 1
    answer = [x,y]
    return answer
   
