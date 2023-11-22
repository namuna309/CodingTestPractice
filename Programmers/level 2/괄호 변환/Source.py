def is_balance(ww):
    cnt = 0
    for c in ww:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
    if cnt == 0:
        return True
    else:
        return False

def is_brokenable(u):
    for i in range(1, len(u) + 1):
        new_u = u[:i]
        new_v = u[i:]
        if is_balance(new_u) and is_balance(new_v):
            if len(new_u) != 0 and len(new_v) == 0:
                return False
    return True
                
    
    
def is_right(u):
    u_stack = []
    for c in u:
        if len(u_stack) == 0:
            u_stack.append(c)
        elif u_stack[-1] == '(' and c == ')':
            u_stack.pop()
        else:
            u_stack.append(c)
    if len(u_stack) == 0:
        return True
    else:
        return False
def reverse(u):
    new_u = ''
    for c in u:
        if c == '(':
            new_u += ')'
        elif c == ')':
            new_u += '('
    
    return new_u

def uddun(w):
    if len(w) == 0:
        return w
    
    # 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    u = ''
    v = ''
    for i in range(1, len(w) + 1):
        u = w[:i]
        v = w[i:]
        if is_balance(u) and is_balance(v) and not is_brokenable(u):
            break
        else:
            continue
            
    
    # 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행 
    if is_right(u):
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환
        u += uddun(v)
        return u
    else:
        # 빈 문자열에 '(', v에 대해 재귀적으로 수행한 결과물 + ')'
        new_w = '(' + uddun(v) + ')'
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 부착
        u = reverse(u[1:-1])
        new_w += u
        return new_w   

def solution(p):

    return uddun(p)

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 9.96MB)
# 테스트 7 〉	통과 (0.05ms, 10.4MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.08ms, 10.4MB)
# 테스트 10 〉	통과 (0.07ms, 10MB)
# 테스트 11 〉	통과 (0.16ms, 10.4MB)
# 테스트 12 〉	통과 (0.56ms, 10.3MB)
# 테스트 13 〉	통과 (0.56ms, 9.96MB)
# 테스트 14 〉	통과 (0.69ms, 10.2MB)
# 테스트 15 〉	통과 (1.15ms, 10.1MB)
# 테스트 16 〉	통과 (4.12ms, 10.2MB)
# 테스트 17 〉	통과 (11.69ms, 10.1MB)
# 테스트 18 〉	통과 (25.61ms, 10.3MB)
# 테스트 19 〉	통과 (10.32ms, 10.2MB)
# 테스트 20 〉	통과 (10.07ms, 10.2MB)
# 테스트 21 〉	통과 (33.00ms, 10.2MB)
# 테스트 22 〉	통과 (6.21ms, 10.4MB)
# 테스트 23 〉	통과 (3.28ms, 10.2MB)
# 테스트 24 〉	통과 (9.55ms, 10.3MB)
# 테스트 25 〉	통과 (16.55ms, 10.3MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0