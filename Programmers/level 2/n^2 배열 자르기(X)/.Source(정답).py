def solution(n, left, right):
    answer = []

    for i in range(0, 16 + 1):
        a = i // n
        b = i % n
        answer.append(max(i // n, i % n) + 1)

    return answer

print(solution(4, 7, 14))