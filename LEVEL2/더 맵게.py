## 더 맵게 - 힙(Heap)
## https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # minheap
    while scoville[0] < K : # 최솟값이 K보다 작을 때
        if len(scoville) == 1: # -1 조건
            return -1
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min_1 + min_2 * 2)
        answer += 1
    return answer
  
  
