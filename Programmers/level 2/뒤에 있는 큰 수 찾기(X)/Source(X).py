def solution(numbers):
    answer = []
    mn = -1
    for i in range(len(numbers) - 1):
        bb = True
        if mn <= numbers[i]:
            ll = numbers[i + 1:]
            for j in range(len(ll)):
                if numbers[i] < ll[j]:
                    answer.append(ll[j])
                    mn = ll[j]
                    bb = False
                    break
        else:
            answer.append(mn)
            bb = False        
        if bb:
            answer.append(-1)
    answer.append(-1)
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	실패 (0.01ms, 10.1MB)
# 테스트 3 〉	실패 (0.01ms, 10.3MB)
# 테스트 4 〉	실패 (0.04ms, 10.3MB)
# 테스트 5 〉	실패 (0.19ms, 10.4MB)
# 테스트 6 〉	실패 (2.49ms, 11.6MB)
# 테스트 7 〉	실패 (2.18ms, 11.4MB)
# 테스트 8 〉	실패 (30.65ms, 17.3MB)
# 테스트 9 〉	실패 (16.79ms, 17.4MB)
# 테스트 10 〉	실패 (95.15ms, 19.9MB)
# 테스트 11 〉	실패 (61.78ms, 19.8MB)
# 테스트 12 〉	실패 (182.50ms, 26.1MB)
# 테스트 13 〉	실패 (242.42ms, 26MB)
# 테스트 14 〉	실패 (1077.45ms, 44.4MB)
# 테스트 15 〉	실패 (3688.44ms, 80.4MB)
# 테스트 16 〉	실패 (4547.70ms, 79.6MB)
# 테스트 17 〉	실패 (4354.33ms, 79MB)
# 테스트 18 〉	실패 (3429.27ms, 81.2MB)
# 테스트 19 〉	실패 (2785.87ms, 80.5MB)
# 테스트 20 〉	통과 (182.62ms, 51.1MB)
# 테스트 21 〉	실패 (시간 초과)
# 테스트 22 〉	실패 (137.83ms, 42.8MB)
# 테스트 23 〉	실패 (시간 초과)

# 채점 결과
# 정확성: 8.7
# 합계: 8.7 / 100.0