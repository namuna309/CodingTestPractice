from collections import deque

def solution(progresses, speeds):
    answer = []
    ps = deque()
    sp = deque()
    for progress, speed in zip(progresses, speeds):
        ps.append(progress)
        sp.append(speed)
    pc = 0
    while ps:
        for i in range(len(ps)):
            ps[i] += sp[i]
        cnt = 0
        ps_done = False
        while ps and ps[0] >= 100 :
            ps_done = True
            ps.popleft()
            sp.popleft()
            cnt += 1
        if ps_done:
            answer.append(cnt)
            ps_done = False
        pc += 1
    return answer