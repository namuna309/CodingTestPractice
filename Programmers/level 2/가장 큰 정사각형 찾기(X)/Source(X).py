def solution(board):
    l = 1        
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + l < len(board) and j + l < len(board[i]):
                b = [board[i][j:j+l] for i in range(i, i + l)]
                one = [[1] * l for _ in range(l)]
                while b == one:
                    if i + l + 1 <= len(board) and j + l + 1 <= len(board[i]):
                        l += 1
                    else:
                        break
                    b = [board[i][j:j+l] for i in range(i, i + l)]
                    one = [[1] * l for _ in range(l)]
                
    return l * l

# 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.4MB)
# 테스트 2 〉	실패 (0.12ms, 10.3MB)
# 테스트 3 〉	통과 (0.07ms, 10.1MB)
# 테스트 4 〉	실패 (0.05ms, 10.2MB)
# 테스트 5 〉	통과 (0.08ms, 10.2MB)
# 테스트 6 〉	실패 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	실패 (0.21ms, 10.3MB)
# 테스트 9 〉	실패 (0.04ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	실패 (0.04ms, 10.2MB)
# 테스트 13 〉	실패 (0.02ms, 10.3MB)
# 테스트 14 〉	실패 (0.10ms, 10.3MB)
# 테스트 15 〉	실패 (0.08ms, 10.2MB)
# 테스트 16 〉	실패 (0.12ms, 10.1MB)
# 테스트 17 〉	실패 (0.05ms, 10.2MB)
# 테스트 18 〉	실패 (2.73ms, 10.2MB)
# 테스트 19 〉	실패 (4.12ms, 10.2MB)

# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)

# 채점 결과
# 정확성: 18.8
# 효율성: 0.0
# 합계: 18.8 / 100.0