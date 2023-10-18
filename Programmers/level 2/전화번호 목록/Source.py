def solution(phone_book):
    pb = sorted(phone_book)
    
    h = pb[0]
    for i in range(1, len(pb)):
        if h in pb[i][:len(h)]:
            return False
        h = pb[i]
            
    return True