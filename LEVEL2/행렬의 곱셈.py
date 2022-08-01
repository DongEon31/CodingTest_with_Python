## 행렬의 곱셈
## https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):    
    arr1_row, mid, arr2_col = len(arr1), len(arr2), len(arr2[0])
    answer = [[0 for _ in range(arr2_col)] for _ in range(arr1_row) ]
    
    for i in range(arr1_row):
        for j in range(arr2_col):
            for m in range(mid):
                answer[i][j] += arr1[i][m] * arr2[m][j]
    
    return answer
  
  
