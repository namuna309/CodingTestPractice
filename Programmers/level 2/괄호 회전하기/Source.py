def check_ss(ss):
    stk = []
    
    for c in ss:
        if len(stk) == 0:
            stk.append(c)
        elif stk[-1] == '[' and c == ']':
            stk.pop(-1)
        elif stk[-1] == '{' and c == '}':
            stk.pop(-1)
        elif stk[-1] == '(' and c == ')':
            stk.pop(-1)
        else:
            stk.append(c)
    
    return False if stk else True
        

def solution(s):
    cnt = 0
    ss = []
    ll = len(s)
    for i in range(ll):
        ss = s[i:] + s[:i]
        if check_ss(ss):
            cnt += 1
    
    return cnt