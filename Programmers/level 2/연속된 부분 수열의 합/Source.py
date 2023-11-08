def solution(sequence, k):
    answer = []
    l = 0
    r = 0
    total = sequence[r]
    
    while r < len(sequence) and l < len(sequence):
        if total == k:
            answer.append([l, r])
        if total <= k:
            r += 1
            if r < len(sequence):
                total += sequence[r]
        elif total > k:
            total -= sequence[l]
            if l < len(sequence):
                l += 1
            
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]