def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)
    
    while dp:
        if y in dp:
            return answer
        else:
            dp_y = set()
            for i in dp:
                if i+n <= y:
                    dp_y.add(i+n)
                if i*2 <= y:
                    dp_y.add(i*2)
                if i*3 <= y:
                    dp_y.add(i*3)
            dp = dp_y
            answer += 1
            
    return -1

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (128.13ms, 26.1MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (119.67ms, 24.4MB)
# 테스트 8 〉	통과 (0.00ms, 10.3MB)
# 테스트 9 〉	통과 (609.05ms, 84.2MB)
# 테스트 10 〉	통과 (498.84ms, 84.1MB)
# 테스트 11 〉	통과 (162.77ms, 37.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (2.44ms, 10.5MB)
# 테스트 15 〉	통과 (0.21ms, 10.4MB)
# 테스트 16 〉	통과 (0.77ms, 10.4MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0