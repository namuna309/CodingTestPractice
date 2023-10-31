from itertools import permutations

def solution(numbers):
    answer = ''
    nums = [str(i) for i in numbers]
    nls = list(permutations(nums, len(nums)))
    ns = []
    for nl in list(nls):
        ns.append(int((''.join(nl))))
        
    return str(max(ns))

# 정확성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	통과 (0.04ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.3MB)
# 테스트 14 〉	통과 (2.47ms, 10.9MB)
# 테스트 15 〉	통과 (0.02ms, 10.3MB)
#
# 채점 결과
# 정확성: 26.7
# 합계: 26.7 / 100.0
