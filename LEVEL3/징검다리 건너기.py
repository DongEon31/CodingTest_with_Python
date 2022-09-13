##  징검다리 건너기 - 2019 카카오 개발자 겨울 인턴십
##  https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0
    # answer는 1명 ~ max(stones) 사이
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        streak = 0
        # 건널 수 있는 연속check
        for stone in stones:
            if streak < k:
                if stone<=mid:
                    streak += 1
                else:
                    streak = 0
            else:
                break
        
        if streak >= k: # 이보다 많이 건널 수 없음 ==> mid 왼쪽 part Search
            right = mid - 1
            answer = mid
        else: # streak < k : 더 많은 사람이 건널 수 있음 ==> mid 오른쪽 part Search
            left = mid + 1
    return answer
