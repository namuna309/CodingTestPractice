def cal_max(land, depth, max_len, i, v):
    s = 0
    if depth == max_len:
        return v
    for j in range(len(land[depth])):
        if j == i:
            continue
            
        s = max(s, cal_max(land, depth + 1, max_len, j, v + land[depth][j]))
        
    return s
        
def solution(land):
    answer = 0
    max_v = -987654321
    for i in range(len(land[0])):
        v = cal_max(land, 1, len(land), i, land[0][i])
        max_v = max(max_v, v)
    
    return max_v

# 정확성  테스트
# 테스트 1 〉	실패 (런타임 에러)
# 테스트 2 〉	실패 (런타임 에러)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (런타임 에러)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (런타임 에러)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (런타임 에러)
# 테스트 9 〉	실패 (런타임 에러)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (런타임 에러)
# 테스트 12 〉	실패 (런타임 에러)
# 테스트 13 〉	실패 (런타임 에러)
# 테스트 14 〉	실패 (런타임 에러)
# 테스트 15 〉	실패 (런타임 에러)
# 테스트 16 〉	실패 (런타임 에러)
# 테스트 17 〉	실패 (런타임 에러)
# 테스트 18 〉	실패 (런타임 에러)
# 
# 효율성  테스트
# 테스트 1 〉	실패 (런타임 에러)
# 테스트 2 〉	실패 (런타임 에러)
# 테스트 3 〉	실패 (런타임 에러)
# 테스트 4 〉	실패 (런타임 에러)
# 
# 채점 결과
# 정확성: 0.0
# 효율성: 0.0
# 합계: 0.0 / 100.0