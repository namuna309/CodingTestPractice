import math

def solution(w,h):
    answer = 0
    
    a = float(h / w)
    if a == 1:
        answer = w * h - w
    else:
        curY = 0
        prevY = 0
        for x in range(w + 1):
            curY = float(a * x)
            answer += math.ceil(curY) - prevY
            prevY = math.floor(curY)
            
    
    return w * h - answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.44ms, 10.1MB)
# 테스트 2 〉	통과 (2.52ms, 10.2MB)
# 테스트 3 〉	통과 (0.73ms, 10.1MB)
# 테스트 4 〉	통과 (2.51ms, 10.2MB)
# 테스트 5 〉	통과 (1.46ms, 10.1MB)
# 테스트 6 〉	실패 (4.33ms, 10.2MB)
# 테스트 7 〉	실패 (0.00ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	실패 (0.00ms, 10.3MB)
# 테스트 10 〉	통과 (0.04ms, 10.1MB)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	실패 (0.00ms, 10.1MB)
# 테스트 13 〉	통과 (3077.94ms, 10.1MB)
# 테스트 14 〉	실패 (0.00ms, 10.2MB)
# 테스트 15 〉	통과 (4337.71ms, 10.2MB)
# 테스트 16 〉	통과 (26.39ms, 10.2MB)
# 테스트 17 〉	통과 (2485.52ms, 10.1MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 
# 채점 결과
# 정확성: 66.7
# 합계: 66.7 / 100.0
