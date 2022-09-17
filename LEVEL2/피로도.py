## 피로도
## https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
def solution(k, dungeons):
    total = len(dungeons)
    dun = [total - i - 1 for i in range(total)] # 7,6,5,4,...,0
    for i in dun: # return i+1
        for cases in permutations(dun,i+1):
            need = k
            flag = False
            for case in cases: # [1,4,2,5,...] 등 순열 조합
                if need >= dungeons[case][0]:
                    need -= dungeons[case][1]
                else:
                    flag = True
            if flag == False:
                return i + 1
    return 0
  
