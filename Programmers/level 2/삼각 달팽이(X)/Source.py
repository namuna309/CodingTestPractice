def solution(n):
    answer = []
    sqr = [[0] * n for _ in range(n)]
    cnt = 0
    num = 1
    x = 0
    y = 0
    cnt = 0
    sub_cnt = 0
    while num <= 10 :
        if cnt % 3 == 0 :
            sqr[y][x] = num
            y += 1
            if y >= n or sqr[y][x] != 0:
                y -= 1
                cnt += 1
                continue
        elif cnt % 3 == 1:
            sqr[y][x] = num
            x += 1
            if x >= n or sqr[y][x] != 0:
                x -= 2
                y -= 1
                cnt += 1
        elif cnt % 3 == 2:
            sqr[y][x] = num
            y -= 1
            x -= 1
            if x < 0 or y < 0 or sqr[y][x] != 0:
                x += 1
                y += 2
                cnt += 1
                continue
        num += 1
        
    return answer

# 테스트 케이스 실패