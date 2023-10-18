def solution(elements):
    length = len(elements)
    total_set = set()
    
    for i in range(length):
        sub_sum = elements[i]
        total_set.add(sub_sum)
        for j in range(i + 1, i + length):
            sub_sum += elements[j%length]
            total_set.add(sub_sum)
    
    return len(total_set)