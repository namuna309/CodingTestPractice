from math import gcd

def list_gcd(array):
    a = array[0]
    for i in array[1:]:
        a = gcd(a, i)
    return a
def test_gcd(a, array):
    if a == 1:
        return False
    for i in array:
        if i % a == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0

    a_gcd = list_gcd(arrayA)
    b_gcd = list_gcd(arrayB)
    test_a_gcd = test_gcd(a_gcd, arrayB)
    test_b_gcd = test_gcd(b_gcd, arrayA)
    
    if test_a_gcd and test_b_gcd:
        return max(a_gcd, b_gcd)
    elif test_a_gcd:
        return a_gcd
    elif test_b_gcd:
        return b_gcd
    else:
         return 0
    
# 정확성  테스트
# 테스트 1 〉	통과 (0.25ms, 10.3MB)
# 테스트 2 〉	통과 (0.67ms, 10.3MB)
# 테스트 3 〉	통과 (0.09ms, 10.2MB)
# 테스트 4 〉	통과 (14.16ms, 12.9MB)
# 테스트 5 〉	통과 (2.02ms, 10.4MB)
# 테스트 6 〉	통과 (4.35ms, 11.2MB)
# 테스트 7 〉	통과 (0.29ms, 10.3MB)
# 테스트 8 〉	통과 (0.42ms, 10.2MB)
# 테스트 9 〉	통과 (1.37ms, 10.6MB)
# 테스트 10 〉	통과 (0.14ms, 10.3MB)
# 테스트 11 〉	통과 (170.41ms, 53.4MB)
# 테스트 12 〉	통과 (145.48ms, 53.4MB)
# 테스트 13 〉	통과 (192.36ms, 53.4MB)
# 테스트 14 〉	통과 (161.47ms, 53.4MB)
# 테스트 15 〉	통과 (187.21ms, 53.4MB)
# 테스트 16 〉	통과 (150.29ms, 53.4MB)
# 테스트 17 〉	통과 (92.41ms, 53.5MB)
# 테스트 18 〉	통과 (119.14ms, 53.4MB)
# 테스트 19 〉	통과 (0.00ms, 10.2MB)
# 테스트 20 〉	통과 (0.00ms, 10.3MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.2MB)
# 테스트 24 〉	통과 (0.01ms, 10.3MB)
# 테스트 25 〉	통과 (0.01ms, 10.3MB)
# 테스트 26 〉	통과 (0.01ms, 10.1MB)
# 테스트 27 〉	통과 (0.04ms, 10.2MB)
# 테스트 28 〉	통과 (0.04ms, 10.3MB)
# 테스트 29 〉	통과 (0.01ms, 10.2MB)
# 테스트 30 〉	통과 (0.01ms, 10.3MB)
# 테스트 31 〉	통과 (0.01ms, 10.3MB)
# 테스트 32 〉	통과 (0.01ms, 10.3MB)
# 테스트 33 〉	통과 (0.01ms, 10.2MB)
# 테스트 34 〉	통과 (0.01ms, 10.3MB)
# 테스트 35 〉	통과 (0.01ms, 10.4MB)
# 테스트 36 〉	통과 (0.01ms, 10.3MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0