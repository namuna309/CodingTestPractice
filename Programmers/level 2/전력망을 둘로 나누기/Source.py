from collections import deque

def solution(n, wires):    
    wds = []
    cnts = []
    for k in range(len(wires)):
        wd = {}
        for i in range(len(wires)):
            if i == k:
                continue
            if wires[i][0] not in wd:
                wd[wires[i][0]] = [wires[i][1]]
            else:
                wd[wires[i][0]].append(wires[i][1])
            if wires[i][1] not in wd:
                wd[wires[i][1]] = [wires[i][0]]
            else:
                wd[wires[i][1]].append(wires[i][0])
        wds.append(wd)
            
    for i in range(len(wires)):
        cnt = []
        wd = wds[i]
        for j in range(2):
            elec = deque()
            elec.append((wires[i][j], 0))
            c = 0
            while elec:
                cn, pn = elec.popleft()
                
                if cn in wd:
                    for nn in wd[cn]:
                        if pn == nn:
                            continue
                        elec.append((nn, cn))
                        c += 1
                else:
                    c = 0        
            cnt.append(c)
        cnts.append(cnt)
        
    min_diff = 987654321    
    for cnt in cnts:
        diff = max(cnt) - min(cnt)
        min_diff = min(min_diff, diff)
            
    return min_diff