def is_square(y, x, board):
    dd = [(1, 0), (0, 1), (1, 1)]
    for d in dd:
        dy, dx = d
        ny = y + dy
        nx = x + dx
        
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[y]):
            return False
        if board[y][x] != board[ny][nx]:
            return False
        if board[y][x] == None:
            return False
    return True
    

def solution(m, n, board):
    answer = 0
    
    nb = []
    for i in range(m):
        l = []
        for j in range(n):
            l.append(board[i][j])
        nb.append(l)
    board = nb
    
    
    while True:
        filters = set()
        dd = [(0, 0), (1, 0), (0, 1), (1, 1)]
        for y in range(m) :
            for x in range(n):
                if board[y][x] != None and is_square(y, x, board):
                    for d in dd:
                        filters.add((y + d[0], x + d[1]))

        if len(filters) == 0:
            break
        answer += len(filters)

        for ft in filters:
            board[ft[0]][ft[1]] = None  
            
        for j in range(n):
            for i in range(m):
                if board[i][j] == None:
                    y = i
                    while y > 0:
                        board[y][j] = board[y - 1][j]
                        board[y - 1][j] = None
                        y -= 1
            
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.11ms, 10.2MB)
# 테스트 2 〉	통과 (0.09ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (4.10ms, 10.4MB)
# 테스트 5 〉	통과 (350.67ms, 10.4MB)
# 테스트 6 〉	통과 (17.95ms, 10.2MB)
# 테스트 7 〉	통과 (2.02ms, 10.3MB)
# 테스트 8 〉	통과 (4.90ms, 10.2MB)
# 테스트 9 〉	통과 (0.06ms, 10.2MB)
# 테스트 10 〉	통과 (1.85ms, 10.3MB)
# 테스트 11 〉	통과 (8.51ms, 10.2MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0