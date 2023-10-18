def solution(msg):
    answer = []
    eng_dict = {}
    eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pl = []
    for i in range(1, len(eng) + 1):
        eng_dict[eng[i - 1]] = i
        
    left = 0
    right = 0
    cur_s = ''
    while True:
        right += 1
        if right == len(msg):
            pl.append(eng_dict[msg[left:right]])
            break
        if msg[left:right+1] not in eng_dict:
            eng_dict[msg[left:right+1]] = len(eng_dict) + 1
            pl.append(eng_dict[msg[left:right]])
            left = right
    
    return pl