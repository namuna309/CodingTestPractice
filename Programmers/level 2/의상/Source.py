def solution(clothes):
    closet = {}
    for cloth in clothes:
        if cloth[1] not in closet:
            closet[cloth[1]] = ["nothing"]
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]].append(cloth[0])
    
    cnt = 1
    
    for n in closet.values():
        cnt *= len(list(n))
    
    return cnt - 1