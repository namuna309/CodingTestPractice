from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    thru = []
    sec = 0
    thru_sum = 0
    
    while thru != truck_weights:
        thing = bridge.popleft()
        thru_sum -= thing
        if len(trucks) != 0 and thru_sum + trucks[0] <= weight:
            thru_sum += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
            
        if thing:
            thru.append(thing)
            
        sec += 1
        
    return sec

# 정확성  테스트
# 테스트 1 〉	통과 (0.71ms, 10.1MB)
# 테스트 2 〉	통과 (10.08ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (8.55ms, 10.3MB)
# 테스트 5 〉	통과 (79.40ms, 10.3MB)
# 테스트 6 〉	통과 (22.93ms, 10.2MB)
# 테스트 7 〉	통과 (0.51ms, 10.2MB)
# 테스트 8 〉	통과 (0.11ms, 10.1MB)
# 테스트 9 〉	통과 (2.92ms, 10.3MB)
# 테스트 10 〉	통과 (0.13ms, 10.3MB)
# 테스트 11 〉	통과 (0.01ms, 10MB)
# 테스트 12 〉	통과 (0.21ms, 10.3MB)
# 테스트 13 〉	통과 (0.79ms, 10.3MB)
# 테스트 14 〉	통과 (0.03ms, 10.2MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0