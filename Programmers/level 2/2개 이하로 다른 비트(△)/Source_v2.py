def make_bin(n):
    b = format(n, "b")
    b = '0' + b
    return [c for c in b]


def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        else:
            n_b = make_bin(number)
            for i in range(1, len(n_b) + 1):
                z = 0
                if n_b[i * (-1)] == '0':
                    z = -1 * i
                    n_b[z] = '1'
                    n_b[z + 1] = '0'
                    break
            b = ''.join(n_b)
            answer.append(int(b, 2))
                    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.83ms, 10.4MB)
# 테스트 2 〉	통과 (95.78ms, 22.8MB)
# 테스트 3 〉	통과 (0.20ms, 10.2MB)
# 테스트 4 〉	통과 (0.93ms, 10.3MB)
# 테스트 5 〉	통과 (0.92ms, 10.4MB)
# 테스트 6 〉	통과 (0.84ms, 10.3MB)
# 테스트 7 〉	통과 (126.65ms, 23.1MB)
# 테스트 8 〉	통과 (123.34ms, 22.4MB)
# 테스트 9 〉	통과 (119.23ms, 22.3MB)
# 테스트 10 〉	통과 (528.66ms, 23.8MB)
# 테스트 11 〉	통과 (556.23ms, 23.9MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0