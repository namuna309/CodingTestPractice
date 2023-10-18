def solution(elements):
    double_elements = elements + elements
    sub_list = []
    total_list = []
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            start = j
            end = j + i
            sub_list = double_elements[start:end]
            total_list.append(sum(sub_list))
    
    return len(set(total_list))