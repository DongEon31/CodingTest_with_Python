## 캐시 - 2018 KAKAO BLIND RECRUITMENT 
## https://school.programmers.co.kr/learn/courses/30/lessons/17680

# using queue

from collections import deque
def solution(cacheSize, cities):
    cache = deque() # 최근 : append / 오래된 것 : popleft
    time = 0
    if cacheSize == 0: # cacheSize가 0이면 매 실행시간은 5
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower() # 대소문자 구분 없음
        if city in cache: # cache hit! city를 맨 앞으로. 
            time += 1
            cache.remove(city)
            cache.append(city)
        else: # cache miss! city를 추가.
            time += 5
            if len(cache) == cacheSize: # cache 꽉 찼으면 오래된 캐시 제거.
                cache.popleft()
            cache.append(city)
    return time
  
  #######################################################################################################################
  #######################################################################################################################
  
  # not using queue
  def solution(cacheSize, cities):
    cache = [] # 최근 : append / 오래된 것 : popleft
    time = 0
    if cacheSize == 0: # cacheSize가 0이면 매 실행시간은 5
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower() # 대소문자 구분 없음
        if city in cache: # cache hit! city를 맨 앞으로. 
            time += 1
            cache.remove(city)
            cache.append(city)
        else: # cache miss! city를 추가.
            time += 5
            if len(cache) == cacheSize: # cache 꽉 찼으면 오래된 캐시 제거.
                cache.pop(0)
            cache.append(city)
    return time
  
