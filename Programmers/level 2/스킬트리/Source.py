from collections import deque

def solution(skill, skill_trees):
    cnt = 0
    
    for skill_tree in skill_trees:
        ss = deque(skill)
        availabe = True
        for i in range(len(skill_tree)):
            if skill_tree[i] in ss:
                if skill_tree[i] == ss[0]:
                    ss.popleft()
                else:
                    availabe = False
                    break    
            if len(ss) == 0:
                break
        if availabe:
            cnt += 1
        
    return cnt