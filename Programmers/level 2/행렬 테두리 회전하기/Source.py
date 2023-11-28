def renew_sqr(p, rot, square):
    y1, x1, y2, x2= p
    y1 -= 1
    y2 -= 1
    x1 -= 1
    x2 -= 1
    cnt = 0
    
    for i in range(x1, x2):
        square[y1][i] = rot[cnt]
        cnt += 1
    for i in range(y1, y2):
        square[i][x2] = rot[cnt]
        cnt += 1
    for i in range(x2, x1, -1):
        square[y2][i] = rot[cnt]
        cnt += 1
    for i in range(y2, y1, -1):
        square[i][x1] = rot[cnt]
        cnt += 1
        
    return square

def extract_rot(p, square):
    y1, x1, y2, x2= p
    y1 -= 1
    y2 -= 1
    x1 -= 1
    x2 -= 1
    
    ex = []
    for i in range(x1, x2):
        ex.append(square[y1][i])
    for i in range(y1, y2):
        ex.append(square[i][x2])
    for i in range(x2, x1, -1):
        ex.append(square[y2][i])
    for i in range(y2, y1, -1):
        ex.append(square[i][x1])
        
    new_ex = [ex[-1]] + ex[:-1]
    return new_ex, min(ex)

def solution(rows, columns, queries):
    answer = []
    ml = []
    cnt = 1
    square = []
    for i in range(rows):
        rl = []
        for j in range(columns):
            rl.append(cnt)
            cnt += 1
        square.append(rl)
    for i in range(len(queries)):
        rot_list, m = extract_rot(queries[i], square)
        ml.append(m)
        square = renew_sqr(queries[i], rot_list, square)
    
    
    return ml