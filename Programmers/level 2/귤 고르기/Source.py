# 초안
def solution(k, tangerine):
    answer = 0
    tangerine_cnt = collections.Counter(tangerine)
    for i in range(len(tangerine)):
        if tangerine[i] not in tangerine_dict:
            tangerine_dict[tangerine[i]] = 1
        else:
            tangerine_dict[tangerine[i]] += 1
    
    tangerines = sorted(tangerine_dict.items(), key = lambda item: -item[1])
    for i in range(len(tangerines)):
        answer += 1
        k -= tangerines[i][1]
        if k <= 0:
            break
            
    return answer

# 개선
import collections

def solution(k, tangerine):
    answer = 0
    tangerine_cnt = collections.Counter(tangerine)
    
    tangerines = sorted(tangerine_cnt.values(), reverse = True)
    for i in range(len(tangerines)):
        answer += 1
        k -= tangerines[i]
        if k <= 0:
            break
            
    return answer