## 타겟 넘버
## https://school.programmers.co.kr/learn/courses/30/lessons/43165

## DFS

def dfs(numbers, target, length):
    answer=0
    if length==len(numbers): # 마지막 도착
        if sum(numbers) == target: # Target과 일치?
            return 1
        else: return 0
    else:
        answer += dfs(numbers,target,length+1) # +number
        numbers[length] *= -1
        answer += dfs(numbers,target,length+1) # -number
        return answer
    
def solution(numbers, target):
    answer = dfs(numbers,target,0)
    return answer
  
###########################################################################################################################################
###########################################################################################################################################

## BFS

def solution(numbers, target):
    answer = 0
    sum_list = [0]
    for num in numbers:
        temp = []
        for t in sum_list:
            temp.append(t + num)
            temp.append(t - num)
        sum_list = temp
    for sums in sum_list:
        if sums == target:
            answer += 1
    return answer
