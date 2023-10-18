from collections import deque

def solution(numbers, target):
    que = deque()
    l = 0
    que.append((0, l))
    tl_lst = []
    while True:
        v, l = que.popleft()
        if l >= len(numbers):
            break
        for i in [-1, 1]:
            que.append((v + numbers[l] * i, l + 1))
            if l == len(numbers) - 1:
                tl_lst.append(v + numbers[l] * i)
    
    cnt = 0
    for n in tl_lst:
        if n == target:
            cnt += 1

    return cnt