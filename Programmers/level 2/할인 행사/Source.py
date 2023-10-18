from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_cnt = {want[i]: number[i] for i in range(len(want))}
    
    for i in range(len(discount) - 9):
        dd = Counter(discount[i: i + 10])
        if dd == want_cnt:
            answer += 1
    
    
    return answer