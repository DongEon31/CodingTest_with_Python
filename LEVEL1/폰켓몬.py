## 폰켓몬
## https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    list = []
    # list인 nums를 set로 만드는 과정인데, 그냥 set(nums)를 써도 됨
    for num in nums:
        if num not in list :
            list.append(num)
 
    return min(len(nums)/2,len(list))

