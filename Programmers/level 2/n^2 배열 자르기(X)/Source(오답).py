def solution(n, left, right):
    result = []
    l_y = left // n 
    l_x = left % n
    r_y = right // n
    r_x = right % n
    
    
    ll = []
    ml = []
    rl = []
    if l_y == r_y:
        rl += [r_y + 1 for i in range(l_x, r_y + 1) if i <= r_x and i <= r_y]
        if r_x > r_y:
            rl += [i + 1 for i in range(len(rl), n)]
            
    else:        
        if l_x <= l_y:
            ll += [l_y + 1 for i in range(l_x, l_y + 1) if i <= l_x and i <= l_y]
        else:
            ll += [i for i in range(l_x + 1, n + 1)]

        for y in range(l_y + 1, r_y):
            ml += [y + 1] * (y + 1) + [i for i in range(y + 2, n + 1)]


        rl += [r_y + 1 for i in range(r_y + 1) if i <= r_x and i <= r_y]
        if r_x > r_y:
            rl += [i + 1 for i in range(len(rl), n)]
    
    
    
    result = ll + ml + rl
    
    
    return result