

def solution(dirs):
    
    maps = [[True for i in range(11)] for j in range(11)]
    x, y = 5, 5
    cnt = 0
    maps[y][x] = False
    his = []
    for i in range(len(dirs)):
        ny = y + d[dirs[i]][1]
        nx = x + d[dirs[i]][0]
        if ny >= len(maps) or ny < 0 or nx >= len(maps) or nx < 0:
            continue
        line = [(y, x), (ny, nx)]
        line.sort()
        if line not in his:
            his.append(line)
            cnt += 1
        y, x = ny, nx
        
    return cnt

# 정확성  테스트
# 테스트 1 〉	통과 (0.10ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.2MB)
# 테스트 4 〉	통과 (0.63ms, 10.4MB)
# 테스트 5 〉	통과 (0.35ms, 10.2MB)
# 테스트 6 〉	통과 (0.17ms, 10.2MB)
# 테스트 7 〉	통과 (0.06ms, 10.1MB)
# 테스트 8 〉	통과 (0.08ms, 10.2MB)
# 테스트 9 〉	통과 (0.09ms, 10.1MB)
# 테스트 10 〉	통과 (0.13ms, 10.3MB)
# 테스트 11 〉	통과 (0.13ms, 10.1MB)
# 테스트 12 〉	통과 (0.25ms, 10.3MB)
# 테스트 13 〉	통과 (0.20ms, 10.1MB)
# 테스트 14 〉	통과 (0.20ms, 10.3MB)
# 테스트 15 〉	통과 (0.14ms, 10.2MB)
# 테스트 16 〉	통과 (2.49ms, 10.1MB)
# 테스트 17 〉	통과 (1.66ms, 10.3MB)
# 테스트 18 〉	통과 (2.51ms, 10.1MB)
# 테스트 19 〉	통과 (1.31ms, 10.3MB)
# 테스트 20 〉	통과 (2.69ms, 10.1MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0