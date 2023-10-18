from collections import Counter

def solution(s):
    n = '1234567890'
    answer = []
    cnts = {}
    s = s[1:-1]
    numbers =[]
    number_list = []
    number = ''
    is_element = False
    for i in range(len(s)):
        if s[i] == '{':
            is_element = True
            continue
        elif is_element:
            if s[i] in n:
                number += s[i]
            elif s[i] == ',':
                number_list.append(int(number))
                number = ''
            elif s[i] == '}':
                is_element = False
                number_list.append(int(number))
                number = ''
                numbers.append(number_list)
                number_list = []
    
    for i in range(len(numbers)):
        cnt = Counter(numbers[i])
        for el, cc in cnt.items():
                if el not in cnts:
                    cnts[el] = cc
                else:
                    cnts[el] += cc
    
    cnts = sorted(cnts.items(), key = lambda x: -x[1])
    answer = [num for num, cnt in cnts]
    return answer