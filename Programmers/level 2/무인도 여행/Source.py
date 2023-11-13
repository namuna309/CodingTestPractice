import sys
     
def dfs(y, x):
    if not v[y][x]:
        return
    v[y][x] = False
    
    cnt = int(m[y][x])
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if ny >= len(m) or ny < 0 or nx >= len(m[0]) or nx < 0:
            continue
        if v[ny][nx] and m[ny][nx] != 'X':
            cnt += dfs(ny, nx)
    return cnt
    

def solution(maps):
    limit_number = 10000
    sys.setrecursionlimit(limit_number)
    answer = []
    global m
    global v
    m = maps
    v = [[True] * len(maps[i]) for i in range(len(maps))]
    cnt = 0
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if v[i][j] and m[i][j] != 'X':
                cnt = dfs(i, j)
                answer.append(cnt)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)


# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.07ms, 10.5MB)
# 테스트 4 〉	통과 (0.20ms, 10.4MB)
# 테스트 5 〉	통과 (1.75ms, 10.7MB)
# 테스트 6 〉	통과 (2.71ms, 10.9MB)
# 테스트 7 〉	통과 (1.52ms, 10.6MB)
# 테스트 8 〉	통과 (4.38ms, 11MB)
# 테스트 9 〉	통과 (11.63ms, 11.6MB)
# 테스트 10 〉	통과 (7.23ms, 11.6MB)
# 테스트 11 〉	통과 (7.69ms, 11.6MB)
# 테스트 12 〉	통과 (10.20ms, 12.7MB)
# 테스트 13 〉	통과 (9.99ms, 12.7MB)
# 테스트 14 〉	통과 (14.35ms, 14.1MB)
# 테스트 15 〉	통과 (14.07ms, 13.4MB)
# 테스트 16 〉	통과 (17.56ms, 14.6MB)
# 테스트 17 〉	통과 (0.48ms, 10.4MB)
# 테스트 18 〉	통과 (17.39ms, 14.5MB)
# 테스트 19 〉	통과 (18.68ms, 14.8MB)
# 테스트 20 〉	통과 (2.30ms, 10.5MB)
# 테스트 21 〉	통과 (0.89ms, 10.5MB)
# 테스트 22 〉	통과 (0.11ms, 10.4MB)
# 테스트 23 〉	통과 (11.19ms, 10.7MB)
# 테스트 24 〉	통과 (9.66ms, 10.7MB)
# 테스트 25 〉	통과 (0.26ms, 10.4MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0