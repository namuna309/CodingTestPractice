from itertools import permutations

def solution(k, dungeons):
#   "최소 필요 피로도": 해당 던전을 탐험하기 위해 남아 있어야 하는 최소한의 피로도
#   "소모 피로도": 던전을 탐험한 후 소모되는 피로도
#   던전은 하루에 한번씩 탐험 가능
    idx_lst = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    max_cnt = 0
    for lst in idx_lst:
        hp = k
        cnt = 0
        for i in lst:
            if hp >= dungeons[i][0]:
                hp -= dungeons[i][1]
                cnt += 1
            else:
                break
        max_cnt = max(cnt, max_cnt)
                    
    answer = max_cnt
    return answer