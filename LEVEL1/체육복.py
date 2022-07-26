## 체육복
## https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # 잃어버리고, 여벌옷이 있는 사람은 자신이 입게 된다. lost, reserve 중복값 제거.
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    # for문 써서 할거면 꼭 정렬하기...    
    _lost.sort()
    _reserve.sort()
    
    # reserve 앞에서부터 check.
 	for r in _reserve:
        if r - 1 in _lost:
            _lost.remove(r - 1)
        elif r + 1 in _lost:
            _lost.remove(r + 1)
    return n - len(_lost)
  
