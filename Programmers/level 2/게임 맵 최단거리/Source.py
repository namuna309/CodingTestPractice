from collections import deque
def solution(maps):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    que = deque()
    que.append((0, 0, 1))
    visited = [[True] * len(maps[i]) for i in range(len(maps))]
    
    while que:
        y, x, cnt = que.popleft()
        if y == len(maps) - 1 and x == len(maps[y]) - 1:
            return cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny >= len(maps) or ny < 0 or nx >= len(maps[y]) or nx < 0:
                continue
            if maps[ny][nx] and visited[ny][nx]:
                visited[ny][nx] = False
                que.append((ny, nx, cnt + 1))

    return -1

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.06ms, 10.3MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (0.07ms, 10.3MB)
# 테스트 6 〉	통과 (0.11ms, 10.2MB)
# 테스트 7 〉	통과 (0.17ms, 10.3MB)
# 테스트 8 〉	통과 (0.07ms, 10.2MB)
# 테스트 9 〉	통과 (0.07ms, 10.4MB)
# 테스트 10 〉	통과 (0.12ms, 10.3MB)
# 테스트 11 〉	통과 (0.07ms, 10.2MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.05ms, 10.2MB)
# 테스트 14 〉	통과 (0.07ms, 10.1MB)
# 테스트 15 〉	통과 (0.07ms, 10.2MB)
# 테스트 16 〉	통과 (0.02ms, 10.4MB)
# 테스트 17 〉	통과 (0.11ms, 10.4MB)
# 테스트 18 〉	통과 (0.02ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.3MB)
# 테스트 20 〉	통과 (0.01ms, 10.3MB)
# 테스트 21 〉	통과 (0.02ms, 10.3MB)
# 
# 효율성  테스트
# 테스트 1 〉	통과 (17.15ms, 10.4MB)
# 테스트 2 〉	통과 (4.31ms, 10.5MB)
# 테스트 3 〉	통과 (11.19ms, 10.4MB)
# 테스트 4 〉	통과 (6.44ms, 10.4MB)
# 
# 채점 결과
# 정확성: 69.9
# 효율성: 30.1
# 합계: 100.0 / 100.0