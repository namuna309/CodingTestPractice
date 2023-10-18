from collections import deque

def solution(priorities, location):
    
    priorities_sorted = deque(sorted(priorities, reverse = True))
    priorities_queue = deque()
    for i in range(len(priorities)):
        priorities_queue.append((priorities[i], i))
    
    p_stk = []
    while priorities_sorted != priorities_queue:
        process = priorities_queue.popleft()
        push_flag = True
        for j in range(len(priorities_queue)):
            if process[0] < priorities_queue[j][0]:
                priorities_queue.append(process)
                push_flag = False
                break
        if push_flag:
            priorities_sorted.popleft()
            p_stk.append(process)
            
    for i in range(len(priorities_queue)):
        p_stk.append(priorities_queue[i])
        
    for i in range(len(p_stk)):
        if p_stk[i][1] == location:
            return i + 1