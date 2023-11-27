def solution(storey):
    stones = 0
    while storey != 0:
        if storey % 10 == 5:
            stones += 5
            if storey >= 10:
                if (storey // 10) % 10 >= 5:
                    storey = (storey + 10) // 10
                else:
                    storey //= 10
            else:
                storey //= 10
                
        elif storey % 10 > 5:
            stones += 10 - (storey % 10)
            storey = (storey // 10) + 1
        else:
            stones += storey % 10
            storey //= 10
        
    return stones