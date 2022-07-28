## 비밀지도 - 2018 KAKAO BLIND RECRUITMENT 
## https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = bin(arr1[i] | arr2[i])
        temp = temp[2:].zfill(n)
        temp = temp.replace('0',' ').replace('1','#')
        answer.append(temp)
    return answer

  
