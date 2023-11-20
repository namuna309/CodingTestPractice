def transformScore(score):
    score_list = []
    for i in range(len(score)):
        if score[i] == '#':
            score_list[-1] = score_list[-1].lower()
        else:
            score_list.append(score[i])
            
    return ''.join(score_list)

def solution(m, musicinfos):
    equal_list = []
    cnt = 0
    sharps = {'C#': 'c', 
                  'D#': 'd',
                  'F#': 'f',
                  'G#': 'g',
                  'A#': 'a'}
    m = transformScore(m)
    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i].split(',')
        start_t, end_t = musicinfo[0], musicinfo[1]
        title = musicinfo[2]
        score = transformScore(musicinfo[3])
        e_score = ''
        
    #   1. 총 몇 분 재생됐는지 구한다
        start_m, start_s = int(start_t[:2]), int(start_t[-2:])
        end_m, end_s = int(end_t[:2]), int(end_t[-2:])
        minute = end_m - start_m
        sec = end_s - start_s
        t = minute * 60 + sec
        
    #   2. 재생된 시간 만큼 악보 정보를 편집한다(채우거나 자른다)
        if t > len(score):
            e_score = t // len(score) * score + score[: t % len(score)]
        else:
            e_score = score[:t]

    #   3. 편집된 음악안에 기억한 멜로디가 있는지 확인한다
        if m in e_score:
            equal_list.append((t, cnt, title))
            cnt += 1
            
    if len(equal_list):
        equal_list.sort(key = lambda x: (-x[0], x[1]))
        return equal_list[0][2]
    
#   4. 있으면 해당된 제목을 반환하고 없으면 "(None)"을 반환한다
    return '(None)'


# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.6MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.5MB)
# 테스트 5 〉	통과 (0.04ms, 10.4MB)
# 테스트 6 〉	통과 (0.04ms, 10.6MB)
# 테스트 7 〉	통과 (0.09ms, 10.4MB)
# 테스트 8 〉	통과 (0.15ms, 10.6MB)
# 테스트 9 〉	통과 (0.09ms, 10.4MB)
# 테스트 10 〉	통과 (0.18ms, 10.4MB)
# 테스트 11 〉	통과 (0.09ms, 10.6MB)
# 테스트 12 〉	통과 (0.15ms, 10.4MB)
# 테스트 13 〉	통과 (0.09ms, 10.5MB)
# 테스트 14 〉	통과 (0.10ms, 10.4MB)
# 테스트 15 〉	통과 (0.15ms, 10.4MB)
# 테스트 16 〉	통과 (0.10ms, 10.6MB)
# 테스트 17 〉	통과 (0.10ms, 10.4MB)
# 테스트 18 〉	통과 (0.15ms, 10.4MB)
# 테스트 19 〉	통과 (0.30ms, 10.5MB)
# 테스트 20 〉	통과 (0.10ms, 10.3MB)
# 테스트 21 〉	통과 (0.09ms, 10.4MB)
# 테스트 22 〉	통과 (0.09ms, 10.4MB)
# 테스트 23 〉	통과 (0.16ms, 10.5MB)
# 테스트 24 〉	통과 (0.10ms, 10.6MB)
# 테스트 25 〉	통과 (0.05ms, 10.4MB)
# 테스트 26 〉	통과 (0.05ms, 10.4MB)
# 테스트 27 〉	통과 (0.06ms, 10.4MB)
# 테스트 28 〉	통과 (0.06ms, 10.5MB)
# 테스트 29 〉	통과 (4.68ms, 10.5MB)
# 테스트 30 〉	통과 (4.40ms, 10.6MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0