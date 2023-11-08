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
        if sum(que1) > sum(que2):
            n = que1.popleft()
            que2.append(n)
            cnt += 1
        elif sum(que1) < sum(que2):
            n = que2.popleft()
            que1.append(n)
            cnt += 1
        elif sum(que1) == sum(que2):
            return cnt
        if cnt > 300000 * 4:
            return -1
        
# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.11ms, 10.2MB)
# 테스트 6 〉	통과 (0.50ms, 10.1MB)
# 테스트 7 〉	통과 (0.33ms, 10.1MB)
# 테스트 8 〉	통과 (0.60ms, 10.2MB)
# 테스트 9 〉	통과 (2.98ms, 10.2MB)
# 테스트 10 〉	통과 (10.42ms, 10.1MB)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	실패 (시간 초과)
# 테스트 13 〉	통과 (518.91ms, 12.1MB)
# 테스트 14 〉	통과 (315.80ms, 12.1MB)
# 테스트 15 〉	실패 (시간 초과)
# 테스트 16 〉	통과 (2805.54ms, 18.3MB)
# 테스트 17 〉	통과 (606.80ms, 17.7MB)
# 테스트 18 〉	통과 (5351.20ms, 33.1MB)
# 테스트 19 〉	실패 (시간 초과)
# 테스트 20 〉	실패 (시간 초과)
# 테스트 21 〉	실패 (시간 초과)
# 테스트 22 〉	실패 (시간 초과)
# 테스트 23 〉	실패 (시간 초과)
# 테스트 24 〉	실패 (시간 초과)
# 테스트 25 〉	통과 (0.82ms, 10.3MB)
# 테스트 26 〉	통과 (0.20ms, 10.2MB)
# 테스트 27 〉	통과 (0.19ms, 9.93MB)
# 테스트 28 〉	실패 (시간 초과)
# 테스트 29 〉	통과 (0.93ms, 10.9MB)
# 테스트 30 〉	실패 (시간 초과)
# 
# 채점 결과
# 정확성: 63.3
# 합계: 63.3 / 100.0