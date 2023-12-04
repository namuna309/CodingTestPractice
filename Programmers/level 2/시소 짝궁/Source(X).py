from itertools import combinations, product

def solution(weights):
    siso_set = set()
    distance = [2, 3, 4]
    p = list(product(distance, weights))
    comb = list(combinations(p, 2))
    for i in range(len(comb)):
        left_d = comb[i][0][0]
        left_w = comb[i][0][1]
        right_d = comb[i][1][0]
        right_w = comb[i][1][1]
        if {left_w, right_w} in siso_set:
            continue
        
        if left_d * left_w == right_d * right_w:
            siso_set.add((left_w, right_w))
        
    return len(siso_set)

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.4MB)
# 테스트 2 〉	실패 (0.28ms, 10.4MB)
# 테스트 3 〉	실패 (0.55ms, 10.1MB)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	실패 (시간 초과)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
# 테스트 15 〉	실패 (시간 초과)
# 테스트 16 〉	통과 (0.03ms, 10.3MB)
# 테스트 17 〉	통과 (0.05ms, 10.3MB)

# 채점 결과
# 정확성: 17.6
# 합계: 17.6 / 100.0