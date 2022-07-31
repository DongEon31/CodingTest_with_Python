## 주차 요금 계산 - 2022 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/92341

from collections import defaultdict
import math
def solution(fees, records):
    car = list(set(map(lambda x: x.split(' ')[1],records)))
    car_in = defaultdict()
    total_fee = {k:0 for k in car}
    for record in records:
        car = record.split(' ') # car[0] - 시간 / car[1] - 차 번호
        if car[1] not in car_in.keys(): # IN STATE
            car_in[car[1]] = car[0]
        else: # OUT STATE
            out_ = int(car[0].split(':')[0]) * 60 + int(car[0].split(':')[1])
            in_ = int(car_in[car[1]].split(':')[0]) * 60 + int(car_in[car[1]].split(':')[1])
            total_fee[car[1]] += (out_ - in_)
            del car_in[car[1]] # OUT -> car_in 비우기
    
    # records를 모두 돌고 car_in에 남은 것들 => 23:59 OUT 처리 
    for remains in car_in.keys():
        out_ = 23 * 60 + 59
        in_ = int(car_in[remains].split(':')[0]) * 60 + int(car_in[remains].split(':')[1])
        total_fee[remains] += (out_ - in_)
    
    # 누적 시간으로 요금 계산
    result = [] # (car_num, total_fee) tuple
    for case in total_fee.items():
        if case[1] > fees[0]: # 기본시간 초과
            result.append((case[0],fees[1] + (math.ceil((case[1]-fees[0])/fees[2]) * fees[3])))
        else: # 기본시간 이하
            result.append((case[0],fees[1]))
    
    # car number 정렬 -> sorted(result)
    answer = list(map(lambda x: x[1],sorted(result))) 
    return answer
  
  
