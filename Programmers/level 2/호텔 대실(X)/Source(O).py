from heapq import heappop, heappush

def solution(book_time):
    answer = 1
    
    # "HH:MM" → HH * 60 + MM
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()
    
    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    
    while heap:
        heappop(heap)

    return answer

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])

# 정확성  테스트
# 테스트 1 〉	통과 (0.07ms, 10.4MB)
# 테스트 2 〉	통과 (0.27ms, 10.5MB)
# 테스트 3 〉	통과 (1.15ms, 10.7MB)
# 테스트 4 〉	통과 (0.71ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (1.03ms, 10.7MB)
# 테스트 7 〉	통과 (1.52ms, 10.5MB)
# 테스트 8 〉	통과 (0.84ms, 10.4MB)
# 테스트 9 〉	통과 (0.32ms, 10.4MB)
# 테스트 10 〉	통과 (1.01ms, 10.5MB)
# 테스트 11 〉	통과 (1.38ms, 10.6MB)
# 테스트 12 〉	통과 (1.35ms, 10.6MB)
# 테스트 13 〉	통과 (0.22ms, 10.3MB)
# 테스트 14 〉	통과 (1.10ms, 10.6MB)
# 테스트 15 〉	통과 (2.05ms, 10.4MB)
# 테스트 16 〉	통과 (0.44ms, 10.4MB)
# 테스트 17 〉	통과 (1.33ms, 10.6MB)
# 테스트 18 〉	통과 (0.81ms, 10.5MB)
# 테스트 19 〉	통과 (1.27ms, 10.6MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0