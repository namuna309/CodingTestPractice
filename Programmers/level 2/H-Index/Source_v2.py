def solution(citations):
    citations.sort(reverse=True)
    enum = list(enumerate(citations, start=1))
    citations_map = list(map(min, enumerate(citations, start=1)))
    answer = max(citations_map)
    return answer

print(solution([3, 0, 6, 1, 5]))