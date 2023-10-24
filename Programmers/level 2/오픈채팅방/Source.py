def solution(record):
    answer = []
    md = {}
    for r in record:
        state = r.split(' ')
        if state[0] == 'Enter':
            md[state[1]] = state[2]
        elif state[0] == 'Change':
            md[state[1]] = state[2]
    
    for r in record:
        state = r.split(' ')
        if state[1] not in md:
            continue
        if state[0] == 'Enter':
            answer.append(md[state[1]] + '님이 들어왔습니다.')
        elif state[0] == 'Leave':
            answer.append(md[state[1]] + '님이 나갔습니다.')
        
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (0.04ms, 10.2MB)
# 테스트 5 〉	통과 (0.76ms, 10.5MB)
# 테스트 6 〉	통과 (0.81ms, 10.4MB)
# 테스트 7 〉	통과 (0.69ms, 10.3MB)
# 테스트 8 〉	통과 (0.78ms, 10.3MB)
# 테스트 9 〉	통과 (0.85ms, 10.4MB)
# 테스트 10 〉	통과 (0.77ms, 10.4MB)
# 테스트 11 〉	통과 (0.44ms, 10.3MB)
# 테스트 12 〉	통과 (0.60ms, 10.3MB)
# 테스트 13 〉	통과 (0.83ms, 10.3MB)
# 테스트 14 〉	통과 (0.86ms, 10.5MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.08ms, 10.2MB)
# 테스트 18 〉	통과 (0.08ms, 10.2MB)
# 테스트 19 〉	통과 (0.77ms, 10.4MB)
# 테스트 20 〉	통과 (0.73ms, 10.3MB)
# 테스트 21 〉	통과 (0.70ms, 10.4MB)
# 테스트 22 〉	통과 (0.75ms, 10.4MB)
# 테스트 23 〉	통과 (0.90ms, 10.4MB)
# 테스트 24 〉	통과 (0.79ms, 10.5MB)
# 테스트 25 〉	통과 (87.53ms, 39MB)
# 테스트 26 〉	통과 (93.76ms, 39.8MB)
# 테스트 27 〉	통과 (106.28ms, 41.2MB)
# 테스트 28 〉	통과 (106.93ms, 42.5MB)
# 테스트 29 〉	통과 (96.49ms, 42.4MB)
# 테스트 30 〉	통과 (83.39ms, 36.8MB)
# 테스트 31 〉	통과 (79.07ms, 41.3MB)
# 테스트 32 〉	통과 (66.40ms, 38.3MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0