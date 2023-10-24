def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stk = []
    
    for i in range(len(prices)):
        while stk and prices[stk[-1]] > prices[i]:
            start_time = stk[-1]
            answer[stk.pop()] = i - start_time
        stk.append(i)
    while stk:
        start_time = stk[-1]
        answer[stk.pop()] = len(prices) - 1 - start_time
        
    return answer