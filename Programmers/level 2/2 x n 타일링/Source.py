def solution(n):
    num = [0 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if i == 1:
            num[i] = 1
        elif i == 2:
            num[i] = 2
        else:
            num[i] = num[i - 2]%1000000007 + num[i - 1]%1000000007
    return num[-1]%1000000007

# 정확성  테스트
# 테스트 1 〉	통과 (2.08ms, 10.2MB)
# 테스트 2 〉	통과 (0.43ms, 10.2MB)
# 테스트 3 〉	통과 (1.75ms, 10.4MB)
# 테스트 4 〉	통과 (2.71ms, 10.3MB)
# 테스트 5 〉	통과 (0.32ms, 10.2MB)
# 테스트 6 〉	통과 (2.27ms, 10.3MB)
# 테스트 7 〉	통과 (0.34ms, 10.3MB)
# 테스트 8 〉	통과 (1.84ms, 10.3MB)
# 테스트 9 〉	통과 (1.81ms, 10.5MB)
# 테스트 10 〉	통과 (2.89ms, 10.3MB)
# 테스트 11 〉	통과 (1.35ms, 10.4MB)
# 테스트 12 〉	통과 (0.43ms, 10.4MB)
# 테스트 13 〉	통과 (0.59ms, 10.3MB)
# 테스트 14 〉	통과 (1.38ms, 10.3MB)
# 
# 효율성  테스트
# 테스트 1 〉	통과 (5.96ms, 10.7MB)
# 테스트 2 〉	통과 (10.27ms, 11.1MB)
# 테스트 3 〉	통과 (6.85ms, 10.8MB)
# 테스트 4 〉	통과 (4.83ms, 10.5MB)
# 테스트 5 〉	통과 (11.93ms, 11.5MB)
# 테스트 6 〉	통과 (16.02ms, 12.2MB)
# 
# 채점 결과
# 정확성: 70.0
# 효율성: 30.0
# 합계: 100.0 / 100.0