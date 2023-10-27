from collections import deque
def solution(x, y, n):
    cnt = 0
    que = deque()
    que.append((x, cnt))
    if x == y:
        return 0
    while que:
        cx, cc = que.popleft()
            
        for i in range(3):
            nx = 0
            if i == 0:
                nx = cx + n
            if i == 1:
                nx = cx * 2
            if i == 2:
                nx = cx * 3
            if nx > y:
                continue
            if nx == y:
                return cc + 1
            que.append((nx, cc + 1))
    return -1
                
# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (12.30ms, 11.3MB)
# 테스트 15 〉	통과 (0.23ms, 10.3MB)
# 테스트 16 〉	통과 (1.76ms, 10.4MB)
# 
# 채점 결과
# 정확성: 68.8
# 합계: 68.8 / 100.0