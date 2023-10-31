def make_quad(arr):
    quad_lists = []
    
    qls = []
    for i in range(len(arr)//2):
        ql = []
        for j in range(len(arr)//2):
            ql.append(arr[i][j])
        qls.append(ql)
    quad_lists.append(qls)
    
    qls = []
    for i in range(len(arr)//2):
        ql = []
        for j in range(len(arr)//2, len(arr)):
            ql.append(arr[i][j])
        qls.append(ql)
    quad_lists.append(qls)
    
    qls = []
    for i in range(len(arr)//2, len(arr)):
        ql = []
        for j in range(len(arr)//2):
            ql.append(arr[i][j])
        qls.append(ql)
    quad_lists.append(qls)
    
    qls = []
    for i in range(len(arr)//2, len(arr)):
        ql = []
        for j in range(len(arr)//2, len(arr)):
            ql.append(arr[i][j])
        qls.append(ql)
    quad_lists.append(qls)
    
    return quad_lists

def quad(arr):
    s = []
    if len(arr) == 1:
        return str(arr[0][0])
    
    quad_lists = make_quad(arr)
    
    for quad_list in quad_lists:
        s += quad(quad_list)
    
    cnt_0 = 0
    cnt_1 = 0
    for c in s:
        if c == '0':
            cnt_0 +=1
        elif c == '1':
            cnt_1 += 1
    
    if cnt_0 == 0 or cnt_1 == 0:
        return s[0]
    else:
        return s

def solution(arr):
    s = quad(arr)
    cnt_0 = 0
    cnt_1 = 0
    
    for c in s:
        if c == '0':
            cnt_0 +=1
        elif c == '1':
            cnt_1 += 1
            
    return [cnt_0, cnt_1]

# 정확성  테스트
# 테스트 1 〉	통과 (2.36ms, 10.4MB)
# 테스트 2 〉	통과 (2.30ms, 10.3MB)
# 테스트 3 〉	통과 (2.52ms, 10.3MB)
# 테스트 4 〉	통과 (0.98ms, 10.4MB)
# 테스트 5 〉	통과 (752.75ms, 17.6MB)
# 테스트 6 〉	통과 (635.65ms, 15.8MB)
# 테스트 7 〉	통과 (644.20ms, 15.1MB)
# 테스트 8 〉	통과 (679.10ms, 14.9MB)
# 테스트 9 〉	통과 (643.72ms, 14.9MB)
# 테스트 10 〉	통과 (2581.81ms, 29.5MB)
# 테스트 11 〉	통과 (0.52ms, 10.4MB)
# 테스트 12 〉	통과 (0.70ms, 10.2MB)
# 테스트 13 〉	통과 (610.81ms, 15MB)
# 테스트 14 〉	통과 (2594.78ms, 29.4MB)
# 테스트 15 〉	통과 (2684.96ms, 29.5MB)
# 테스트 16 〉	통과 (646.07ms, 15.2MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0