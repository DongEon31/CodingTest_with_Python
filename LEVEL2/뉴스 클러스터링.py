## 뉴스 클러스터링 - 2018 KAKAO BLIND RECRUITMENT
## https://school.programmers.co.kr/learn/courses/30/lessons/17677

from collections import defaultdict
import math
def solution(str1, str2):
    # 알파벳 소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()
    
    inter = [] # 교집합
    sum_ = defaultdict(int) # 합집합
    sum_for_str2 = defaultdict(int) # str2에서 사용하기 위한 dict
    
    # str1 : sum_ 딕셔너리에 count
    for index, alpha in enumerate(str1):
        if index > 0 and str1[index-1].isalpha() and alpha.isalpha():
            sum_[str1[index-1] + alpha] += 1
            
    # str2 : sum_for_str2에 따로 저장하면서, sum_보다 작으면 교집합에 추가 / 크면 합집합에 추가.
    for index, alpha in enumerate(str2):
        if index > 0 and str2[index-1].isalpha() and alpha.isalpha():
            if sum_[str2[index-1]+alpha] > sum_for_str2[str2[index-1]+alpha] : # 교집합 case
                inter.append(str2[index-1]+alpha)                   
            else : # str1보다 str2에 많은 경우 : 합집합 case
                sum_[str2[index-1]+alpha] += 1
            sum_for_str2[str2[index-1]+alpha] += 1
    
    sum_count = 0
    for item in sum_.items(): # 합집합 원소 개수 count
        sum_count += item[1]
    
    # 두 집합이 모두 공집합인 case
    if sum_count==0:
        answer = 65536
    # 일반적인 case : math.floor()로 소수점 버림
    else :
        answer = math.floor((len(inter)/sum_count)*65536)        
    return answer
  
  
