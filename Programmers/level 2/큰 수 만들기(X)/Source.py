from itertools import combinations

def solution(number, k):
    answer = ''
    nums = list(combinations(number, len(number) - k))
    nl = []
    for num in nums:
        nl.append(int(''.join(num)))
    
    answer = str(max(nl))
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.09ms, 10.3MB)
# 테스트 2 〉	통과 (1640.60ms, 578MB)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	통과 (0.02ms, 10.4MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 채점 결과
# 정확성: 33.3
# 합계: 33.3 / 100.0