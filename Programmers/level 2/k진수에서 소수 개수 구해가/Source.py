def is_prime_number(n):
    
    if n < 2:
        return False
    
    for i in range(2, int(n**(1/2)) + 1): 
        if n % i == 0:
            return False

    return True

def nary(n, k):
    s = ''
    while n:
        s += str(n % k)
        n = n // k
    
    return ''.join(reversed(s))

def solution(n, k):
    answer = -1
    
    s = nary(n, k)
    n_list = s.split('0')
    n_list = [int(i) for i in n_list if i != '']
    prime_list = is_prime_number(max(n_list))
    cnt = 0
    print(n_list)
    for ne in n_list:
        if is_prime_number(ne):
            cnt += 1
            
    return cnt