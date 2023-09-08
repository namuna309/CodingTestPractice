def solution(new_id):
    special_char = list("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    new_id = new_id.lower()
    new_id_list = list(new_id)
    idx_list = []
    for i in range(len(new_id_list)):
        if new_id_list[i] not in special_char:
            idx_list.append(i)
    new_id_list = [new_id_list[i] for i in range(len(new_id_list)) if i not in idx_list]
    i = 0
    idx_list = []
    for i in range(len(new_id_list)):
        if new_id_list[i] == '.' and i < len(new_id_list) - 1:
            if new_id_list[i] == new_id_list[i + 1]:
                continue
        idx_list.append(i)
    
    new_id_list = [new_id_list[i] for i in range(len(new_id_list)) if i in idx_list]  
        
    idx_list = []
    for i in range(len(new_id_list)):
        if new_id_list[i] == '.' and (i == 0 or i == len(new_id_list) - 1):
            continue
        idx_list.append(i)
    
    new_id_list = [new_id_list[i] for i in range(len(new_id_list)) if i in idx_list] 
    
    if len(new_id_list) == 0:
        new_id_list.append('a')
    
    if len(new_id_list) >= 16:
        new_id_list = new_id_list[:15]
        if new_id_list[-1] == '.':
            new_id_list = new_id_list[:-1]
            
    while len(new_id_list) <= 2:
        new_id_list.append(new_id_list[-1])
    
    
    return ''.join(new_id_list)