import sys
sys.setrecursionlimit(10**7)

def step_cnt(n, step_dict):
    if n == 1:
        step_dict[n] = 1
    elif n == 2:
        step_dict[n] = 2
    else:
        if n - 1 in step_dict:
            n1 = step_dict[n - 1]
        else:
            n1 = step_cnt(n - 1, step_dict)
        if n - 2 in step_dict:
            n2 = step_dict[n - 2]
        else:
            n2 = step_cnt(n - 2, step_dict)

        sum = n1 % 1234567 + n2 % 1234567
    
        step_dict[n] = sum 
    
    return step_dict[n] % 1234567

def solution(n):
    
    answer = 0
    
    step_dict = {}
    
    answer = step_cnt(n, step_dict)
    
    
    
    return answer