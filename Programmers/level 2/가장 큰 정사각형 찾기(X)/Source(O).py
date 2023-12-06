def solution(board):

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if i - 1 < 0 or j - 1 < 0:
                    continue
                board[i][j] = 1 + min([board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]])
                    
    l = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            l = max(l, board[i][j])
    
    
    return l**2

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.14ms, 10.3MB)
# 테스트 5 〉	통과 (0.07ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.11ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.04ms, 10.2MB)
# 테스트 13 〉	통과 (0.02ms, 10.2MB)
# 테스트 14 〉	통과 (0.05ms, 10.2MB)
# 테스트 15 〉	통과 (0.12ms, 10.2MB)
# 테스트 16 〉	통과 (0.13ms, 10.3MB)
# 테스트 17 〉	통과 (0.07ms, 10.2MB)
# 테스트 18 〉	통과 (1.53ms, 10.2MB)
# 테스트 19 〉	통과 (1.52ms, 10.2MB)

# 효율성  테스트
# 테스트 1 〉	통과 (627.40ms, 31.1MB)
# 테스트 2 〉	통과 (653.31ms, 30.5MB)
# 테스트 3 〉	통과 (650.66ms, 30.7MB)

# 채점 결과
# 정확성: 59.6
# 효율성: 40.4
# 합계: 100.0 / 100.0