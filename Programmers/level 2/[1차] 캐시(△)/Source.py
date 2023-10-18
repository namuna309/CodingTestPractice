from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = deque()
    cacheMiss = 0
    cacheHit = 0
    for i in range(len(cities)):
        city = cities[i].lower()
        if city in cache:
            cacheHit += 1
        else:
            cacheMiss += 5
        if len(cache) < cacheSize:
            cache.append(city)
        else:
            cache.popleft()
            cache.append(city)
    answer = cacheMiss + cacheHit
    return answer