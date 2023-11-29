import heapq

def solution(N, road, K):
    answer = 0
    graph = {}
    graph ={i: [] for i in range(1, N + 1)}
    for r in road:
        graph[r[0]].append((r[2] ,r[1]))
        graph[r[1]].append((r[2], r[0]))

    costs = {}
    pq = []
    heapq.heappush(pq, (0, 1))
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    
    filtered_costs = [(i, j) for i, j in costs.items() if j <= K]
    
    return len(filtered_costs)

# 정확성  테스트
# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.09ms, 10.2MB)
# 테스트 5 〉	통과 (0.04ms, 10.4MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.4MB)
# 테스트 8 〉	통과 (0.03ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.06ms, 10.3MB)
# 테스트 13 〉	통과 (0.10ms, 10.2MB)
# 테스트 14 〉	통과 (2.44ms, 10.7MB)
# 테스트 15 〉	통과 (4.80ms, 10.5MB)
# 테스트 16 〉	통과 (0.06ms, 10.4MB)
# 테스트 17 〉	통과 (0.07ms, 10.2MB)
# 테스트 18 〉	통과 (0.82ms, 10.3MB)
# 테스트 19 〉	통과 (2.71ms, 10.6MB)
# 테스트 20 〉	통과 (0.75ms, 10.3MB)
# 테스트 21 〉	통과 (6.92ms, 11MB)
# 테스트 22 〉	통과 (0.69ms, 10.4MB)
# 테스트 23 〉	통과 (3.38ms, 10.8MB)
# 테스트 24 〉	통과 (2.18ms, 10.4MB)
# 테스트 25 〉	통과 (4.48ms, 10.9MB)
# 테스트 26 〉	통과 (4.39ms, 10.9MB)
# 테스트 27 〉	통과 (5.26ms, 11MB)
# 테스트 28 〉	통과 (4.89ms, 11.1MB)
# 테스트 29 〉	통과 (4.56ms, 10.9MB)
# 테스트 30 〉	통과 (5.29ms, 11MB)
# 테스트 31 〉	통과 (0.06ms, 10.3MB)
# 테스트 32 〉	통과 (0.14ms, 10.2MB)

# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0