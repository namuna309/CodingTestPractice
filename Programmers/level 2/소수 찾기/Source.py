from itertools import permutations
import math
def is_deci(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if i == n: continue
        if n % i == 0:
            return False
    return True


def solution(numbers):
    cnt = 0
    n = len(numbers)
    nums = [c for c in numbers]
    nl = []
    for i in range(1, n + 1):
        ps = set(permutations(nums, i))
        for p in ps:
            nl.append(int(''.join(p)))
    ns = set(nl)
    for n in ns:
        if n <= 1:
            continue
        else:
            if is_deci(n):
                cnt += 1
    return cnt

# 정확성  테스트
# 테스트 1 〉	통과 (0.06ms, 10.3MB)
# 테스트 2 〉	통과 (5.61ms, 10.5MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.40ms, 10.5MB)
# 테스트 5 〉	통과 (0.94ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.06ms, 10.4MB)
# 테스트 8 〉	통과 (1.75ms, 10.3MB)
# 테스트 9 〉	통과 (0.06ms, 10.5MB)
# 테스트 10 〉	통과 (14.30ms, 10.5MB)
# 테스트 11 〉	통과 (1.07ms, 10.5MB)
# 테스트 12 〉	통과 (0.32ms, 10.5MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0