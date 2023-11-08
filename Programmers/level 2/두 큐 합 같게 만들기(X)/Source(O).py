from collections import deque

def solution(queue1, queue2):
    if(sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    que1 = deque(queue1)
    que2 = deque(queue2)
    mid = (sum(que1) + sum(que2)) // 2
    
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    
    cnt = 0
    n = 0
    while True:
        if tot1 > tot2:
            n = que1.popleft()
            que2.append(n)
            tot1 -= n
            tot2 += n
            cnt += 1
        elif tot1 < tot2:
            n = que2.popleft()
            que1.append(n)
            tot1 += n
            tot2 -= n
            cnt += 1
        elif sum(que1) == sum(que2):
            return cnt
        if cnt > 300000 * 4:
            return -1
        

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.2MB)
# 테스트 6 〉	통과 (0.06ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10MB)
# 테스트 9 〉	통과 (0.13ms, 10.2MB)
# 테스트 10 〉	통과 (0.19ms, 10.2MB)
# 테스트 11 〉	통과 (254.69ms, 14.5MB)
# 테스트 12 〉	통과 (8.03ms, 14.4MB)
# 테스트 13 〉	통과 (5.81ms, 12MB)
# 테스트 14 〉	통과 (5.87ms, 12.3MB)
# 테스트 15 〉	통과 (8.92ms, 17.9MB)
# 테스트 16 〉	통과 (7.49ms, 18.5MB)
# 테스트 17 〉	통과 (7.21ms, 17.4MB)
# 테스트 18 〉	통과 (22.25ms, 33MB)
# 테스트 19 〉	통과 (34.73ms, 37.4MB)
# 테스트 20 〉	통과 (40.18ms, 37.6MB)
# 테스트 21 〉	통과 (30.26ms, 37.6MB)
# 테스트 22 〉	통과 (71.21ms, 37.6MB)
# 테스트 23 〉	통과 (53.82ms, 37.9MB)
# 테스트 24 〉	통과 (77.62ms, 38.1MB)
# 테스트 25 〉	통과 (0.05ms, 10.2MB)
# 테스트 26 〉	통과 (0.03ms, 10.2MB)
# 테스트 27 〉	통과 (0.03ms, 10MB)
# 테스트 28 〉	통과 (354.12ms, 19.2MB)
# 테스트 29 〉	통과 (0.69ms, 10.7MB)
# 테스트 30 〉	통과 (49.99ms, 19MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0