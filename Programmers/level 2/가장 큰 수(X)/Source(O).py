def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 정확성  테스트
# 테스트 1 〉	통과 (759.84ms, 23MB)
# 테스트 2 〉	통과 (232.50ms, 17.1MB)
# 테스트 3 〉	통과 (1290.09ms, 27.1MB)
# 테스트 4 〉	통과 (1.64ms, 10.4MB)
# 테스트 5 〉	통과 (631.25ms, 21.5MB)
# 테스트 6 〉	통과 (499.70ms, 20.1MB)
# 테스트 7 〉	통과 (0.03ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (0.02ms, 10.4MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.02ms, 10.2MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0