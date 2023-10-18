def solution(elements):
    double_elements = elements + elements
    total_set = set()
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            start = j
            end = j + i
            total_set.add(sum(double_elements[start:end]))
    
    return len(total_set)