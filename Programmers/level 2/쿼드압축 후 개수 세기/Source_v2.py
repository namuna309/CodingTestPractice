def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.41ms, 10.3MB)
# 테스트 2 〉	통과 (0.35ms, 10.2MB)
# 테스트 3 〉	통과 (0.18ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.2MB)
# 테스트 5 〉	통과 (140.81ms, 12.2MB)
# 테스트 6 〉	통과 (55.82ms, 12.2MB)
# 테스트 7 〉	통과 (36.63ms, 12.2MB)
# 테스트 8 〉	통과 (26.59ms, 12.2MB)
# 테스트 9 〉	통과 (36.14ms, 12.2MB)
# 테스트 10 〉	통과 (117.84ms, 19.2MB)
# 테스트 11 〉	통과 (0.07ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (42.72ms, 12.2MB)
# 테스트 14 〉	통과 (179.56ms, 19.1MB)
# 테스트 15 〉	통과 (230.83ms, 19.2MB)
# 테스트 16 〉	통과 (67.63ms, 12.2MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0