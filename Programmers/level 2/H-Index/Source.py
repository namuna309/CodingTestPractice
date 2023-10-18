def solution(citations):
    citations.sort()
    min_c = citations[0]
    max_c = citations[-1]
    max_h = 0
    for i in range(max_c + 1):
        for j in range(len(citations)):
            if citations[j] >= i and i == len(citations[j:]):
                max_h = max(i, max_h)
                break
        
    return max_h