from collections import Counter

def solution(weights):
    cnt = 0
    w_counter = Counter(weights)
    for k, v in w_counter.items():
        if v >= 2:
            cnt += v * (v - 1) // 2
    w_set = set(weights)
    for w in w_set:
        if w * (2 / 3) in w_set:
            cnt += w_counter[w * (2 / 3)] * w_counter[w]
        if w * (2 / 4) in w_set:
            cnt += w_counter[w * (2 / 4)] * w_counter[w]
        if w * (3 / 4) in w_set:
            cnt += w_counter[w * (3 / 4)] * w_counter[w]
                    
    return cnt

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (1.47ms, 10.7MB)
# 테스트 5 〉	통과 (2.22ms, 10.7MB)
# 테스트 6 〉	통과 (3.32ms, 11.1MB)
# 테스트 7 〉	통과 (3.58ms, 11.4MB)
# 테스트 8 〉	통과 (5.04ms, 12MB)
# 테스트 9 〉	통과 (6.43ms, 12.8MB)
# 테스트 10 〉	통과 (8.68ms, 13.4MB)
# 테스트 11 〉	통과 (8.91ms, 13.4MB)
# 테스트 12 〉	통과 (8.33ms, 14MB)
# 테스트 13 〉	통과 (8.80ms, 13.9MB)
# 테스트 14 〉	통과 (8.76ms, 14MB)
# 테스트 15 〉	통과 (9.04ms, 14.1MB)
# 테스트 16 〉	통과 (0.02ms, 10.4MB)
# 테스트 17 〉	통과 (0.02ms, 10.2MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0