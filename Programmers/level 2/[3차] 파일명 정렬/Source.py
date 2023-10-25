def split_hnt(file):
    head = ''
    number = ''
    tail = ''
    idx = 0
    digit = '0123456789'
    
    for i in range(len(file[idx:])):
        if file[i] not in digit:
            head += file[i]
            idx = i
        else:
            break
    idx += 1
    for i in range(idx, idx + len(file[idx:])):
        if file[i] in digit:
            number += file[i]
            idx = i
        else:
            break
    idx += 1
    tail = file[idx:]
        
    return head, number, tail
    
        

def solution(files):
    answer = []
    files_split = []
    for file in files:
        head, num, tail = split_hnt(file)
        files_split.append((head, num, tail))
    files_split.sort(key = lambda x: (x[0].lower(), int(x[1])))
    
    for file in files_split:
        fn = ''.join(file)
        answer.append(fn)
        
    return answer