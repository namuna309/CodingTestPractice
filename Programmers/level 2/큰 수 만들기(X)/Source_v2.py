def solution(number, k):
    answer = []
    for c in number:
        if len(answer) == 0:
            answer.append(c)
            continue
        if k > 0:
            while answer[-1] < c:
                answer.pop()
                k -= 1
                if k <= 0 or len(answer) == 0:
                    break
        answer.append(c)
    answer = answer[:-k] if k > 0 else answer
    
    return ''.join(answer)

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.2MB)
# 테스트 4 〉	통과 (0.13ms, 10.4MB)
# 테스트 5 〉	통과 (0.23ms, 10.2MB)
# 테스트 6 〉	통과 (3.98ms, 10.3MB)
# 테스트 7 〉	통과 (9.66ms, 10.3MB)
# 테스트 8 〉	통과 (26.10ms, 10.6MB)
# 테스트 9 〉	통과 (60.59ms, 12.7MB)
# 테스트 10 〉	통과 (154.53ms, 13.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
