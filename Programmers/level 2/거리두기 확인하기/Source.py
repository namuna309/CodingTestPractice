from itertools import combinations

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
ddy = [1, 1, -1, -1]
ddx = [1, -1, 1, -1]

def dfs(y, x, visited, ps):
    if visited[y][x]:
        return
    visited[y][x] = True
    if place[y][x] == 'P':
        ps.append((y, x))
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if (ny >= 5 or ny < 0 or nx >= 5 or nx < 0) or visited[ny][nx] :
            continue
        if place[ny][nx] != 'X':
            dfs(ny, nx, visited, ps)
    return ps
    
def solution(places):
    global place
    result = []
    for pl in range(len(places)):
        place = places[pl]
        visited = [[False] * 5 for i in range(5)]
        positions = []

        for i in range(5):
            for j in range(5):
                if visited[i][j] == False and place[i][j] == 'P':
                    p = []
                    ps = dfs(i, j, visited, p)
                    positions.append(ps)
        inbound = False
        for position in positions:  
            for p in position:
                a = 1
                y = p[0]
                x = p[1]
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if nx >= 5 or nx < 0 or ny >= 5 or ny < 0:
                        continue
                    if place[ny][nx] == 'P':
                        inbound = True
                        break
                    if place[ny][nx] == 'O':
                        ny += dy[i]
                        nx += dx[i]
                        if nx < 5 and nx >= 0 and ny < 5 and ny >= 0 and place[ny][nx] == 'P':
                            inbound = True
                            break
                if inbound == False: 
                    for i in range(4):
                        ny = y + ddy[i]
                        nx = x + ddx[i]
                        if nx >= 5 or nx < 0 or ny >= 5 or ny < 0:
                            continue
                        if place[ny][nx] == 'P' and (place[y][nx] != 'X' or place[ny][x] != 'X'):
                            inbound = True
                            break
                if inbound:
                    break
            if inbound:
                break
        if inbound:  
            result.append(0)
        else:
            result.append(1)
    return result


# 정확성  테스트
# 테스트 1 〉	통과 (0.22ms, 10.5MB)
# 테스트 2 〉	통과 (0.11ms, 10.3MB)
# 테스트 3 〉	통과 (0.17ms, 10.1MB)
# 테스트 4 〉	통과 (0.15ms, 10.2MB)
# 테스트 5 〉	통과 (0.13ms, 10.2MB)
# 테스트 6 〉	통과 (0.17ms, 10.3MB)
# 테스트 7 〉	통과 (0.26ms, 10.1MB)
# 테스트 8 〉	통과 (0.29ms, 10.3MB)
# 테스트 9 〉	통과 (0.30ms, 10.4MB)
# 테스트 10 〉	통과 (0.25ms, 10.2MB)
# 테스트 11 〉	통과 (0.27ms, 10.2MB)
# 테스트 12 〉	통과 (0.27ms, 10.3MB)
# 테스트 13 〉	통과 (0.16ms, 10.3MB)
# 테스트 14 〉	통과 (0.11ms, 10.4MB)
# 테스트 15 〉	통과 (0.14ms, 10.2MB)
# 테스트 16 〉	통과 (0.16ms, 10.3MB)
# 테스트 17 〉	통과 (0.27ms, 10.2MB)
# 테스트 18 〉	통과 (0.28ms, 10.4MB)
# 테스트 19 〉	통과 (0.34ms, 10.2MB)
# 테스트 20 〉	통과 (0.21ms, 10.3MB)
# 테스트 21 〉	통과 (0.11ms, 10.2MB)
# 테스트 22 〉	통과 (0.17ms, 10.3MB)
# 테스트 23 〉	통과 (0.04ms, 10.3MB)
# 테스트 24 〉	통과 (0.20ms, 10.1MB)
# 테스트 25 〉	통과 (0.05ms, 10.5MB)
# 테스트 26 〉	통과 (0.05ms, 10.4MB)
# 테스트 27 〉	통과 (0.17ms, 10.1MB)
# 테스트 28 〉	통과 (0.16ms, 10.1MB)
# 테스트 29 〉	통과 (0.14ms, 10.3MB)
# 테스트 30 〉	통과 (0.13ms, 10.2MB)
# 테스트 31 〉	통과 (0.36ms, 10.3MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0