import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2*2)
        answer += 1
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.87ms, 10.3MB)
# 테스트 7 〉	통과 (0.72ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.3MB)
# 테스트 9 〉	통과 (0.07ms, 10.2MB)
# 테스트 10 〉	통과 (0.30ms, 10.2MB)
# 테스트 11 〉	통과 (0.21ms, 10.3MB)
# 테스트 12 〉	통과 (0.74ms, 9.96MB)
# 테스트 13 〉	통과 (0.42ms, 10.1MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.92ms, 10.3MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.3MB)
# 테스트 18 〉	통과 (0.00ms, 10.3MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)
# 테스트 21 〉	통과 (0.00ms, 10.3MB)
# 테스트 22 〉	통과 (0.00ms, 10.1MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.1MB)
# 테스트 25 〉	통과 (0.01ms, 10.1MB)
# 테스트 26 〉	통과 (0.01ms, 10.1MB)
# 
# 효율성  테스트
# 테스트 1 〉	통과 (179.91ms, 16.2MB)
# 테스트 2 〉	통과 (393.52ms, 21.8MB)
# 테스트 3 〉	통과 (1541.01ms, 49.6MB)
# 테스트 4 〉	통과 (131.48ms, 14.9MB)
# 테스트 5 〉	통과 (1842.81ms, 51.7MB)
# 
# 채점 결과
# 정확성: 83.9
# 효율성: 16.1
# 합계: 100.0 / 100.0