def solution(board, moves):
    bucket = []
    answer = 0

    for move in moves:
        for row in range(len(board)):
            if board[row][move - 1] != 0:
                doll = board[row][move - 1]
                board[row][move - 1] = 0

                if len(bucket) == 0 or bucket[-1] != doll:
                    bucket.append(doll)
                elif bucket[-1] == doll:
                    bucket.pop(-1)
                    answer += 2
                break
        
    return answer