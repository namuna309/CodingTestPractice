def solution(data, col, row_begin, row_end):
    answer = 0
    key_row = [i for i in data[0]]
    
    s = sorted(data, key = lambda x: [x[col - 1], -x[0]])
    S = [0] * len(s)
    for i in range(len(s)):
        for j in range(len(s[i])):
            S[i] += s[i][j] % (i + 1)
            
    for i in range(row_begin - 1, row_end):
        answer ^= S[i]
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.1MB)
# 테스트 2 〉	통과 (0.22ms, 10.4MB)
# 테스트 3 〉	통과 (0.17ms, 10.2MB)
# 테스트 4 〉	통과 (1.09ms, 10.3MB)
# 테스트 5 〉	통과 (14.34ms, 12.2MB)
# 테스트 6 〉	통과 (240.91ms, 57.8MB)
# 테스트 7 〉	통과 (263.31ms, 64.5MB)
# 테스트 8 〉	통과 (310.01ms, 64.4MB)
# 테스트 9 〉	통과 (258.35ms, 64.5MB)
# 테스트 10 〉 통과 (340.98ms, 64.3MB)
# 테스트 11 〉 통과 (0.01ms, 10.1MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0