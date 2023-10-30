def make_bin(n):
    b = format(n, "b")
    z = ''
    for _ in range(50 - len(b)):
        z += str(0)
    return z + b


def solution(numbers):
    answer = []
    
    for number in numbers:
        n_b = make_bin(number)
        num = number + 1
        while True:
            
            num_b = make_bin(num)
            cnt = 0
            for i in range(len(num_b)):
                if num_b[i] != n_b[i]:
                    cnt += 1
                if cnt > 2:
                    break
            if cnt <= 2:
                break
            else:
                num += 1
        answer.append(num)
            
                    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (38.03ms, 10.3MB)
# 테스트 2 〉	통과 (5177.97ms, 22.8MB)
# 테스트 3 〉	통과 (14.44ms, 10.3MB)
# 테스트 4 〉	통과 (32.34ms, 10.3MB)
# 테스트 5 〉	통과 (78.55ms, 10.2MB)
# 테스트 6 〉	통과 (54.30ms, 10.3MB)
# 테스트 7 〉	통과 (3992.18ms, 23.7MB)
# 테스트 8 〉	통과 (2476.87ms, 23.2MB)
# 테스트 9 〉	통과 (3256.46ms, 22.9MB)
# 테스트 10 〉	실패 (시간 초과)
# 테스트 11 〉	실패 (시간 초과)
# 
# 채점 결과
# 정확성: 81.8
# 합계: 81.8 / 100.0