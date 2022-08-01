## 불량 사용자 - 2019 카카오 개발자 겨울 인턴십
## https://school.programmers.co.kr/learn/courses/30/lessons/64064


from itertools import permutations
def same(user, banned_id):
    for word in range(len(user)):
        if len(user[word]) != len(banned_id[word]): #1. 길이 check
            return False
        for alpha in range(len(banned_id[word])):
            if banned_id[word][alpha] == '*' or user[word][alpha] == banned_id[word][alpha]: #2. '*'이거나 문자가 같은지 check
                continue    
            else: #3. 하나라도 다르면 False
                return False
    return True        

def solution(user_id, banned_id):
    user_per = list(permutations(user_id,len(banned_id)))
    banned_list = []
    
    # 하나의 튜플과 banned_id 비교
    for user in user_per:
        if same(user,banned_id):
            T = set(user)
            if T not in banned_list:
                banned_list.append(T)  
        else:
            continue
            
    return len(banned_list)
  
