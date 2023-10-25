from collections import Counter

def solution(topping):
    answer = 0
    ls = set(topping)
    ld = Counter(topping)
    rs = set()
    
    for i in range(len(topping)):
        ld[topping[-1]] -= 1
        if ld[topping[-1]] == 0:
            ls.remove(topping[-1])
        rs.add(topping.pop())
        
        if len(ls) == len(rs):
            answer += 1
        
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (10.76ms, 10.7MB)
# 테스트 2 〉	통과 (126.39ms, 15.4MB)
# 테스트 3 〉	통과 (101.90ms, 10.8MB)
# 테스트 4 〉	통과 (85.65ms, 10.8MB)
# 테스트 5 〉	통과 (557.57ms, 18.6MB)
# 테스트 6 〉	통과 (804.67ms, 51.4MB)
# 테스트 7 〉	통과 (779.71ms, 51.3MB)
# 테스트 8 〉	통과 (1001.24ms, 51.4MB)
# 테스트 9 〉	통과 (931.04ms, 50.5MB)
# 테스트 10 〉	통과 (828.45ms, 50.5MB)
# 테스트 11 〉	통과 (64.05ms, 10.8MB)
# 테스트 12 〉	통과 (13.97ms, 11.9MB)
# 테스트 13 〉	통과 (866.05ms, 50.6MB)
# 테스트 14 〉	통과 (848.91ms, 50.5MB)
# 테스트 15 〉	통과 (1021.16ms, 50.5MB)
# 테스트 16 〉	통과 (888.40ms, 50.7MB)
# 테스트 17 〉	통과 (1318.73ms, 50.5MB)
# 테스트 18 〉	통과 (923.04ms, 51.3MB)
# 테스트 19 〉	통과 (952.16ms, 51.3MB)
# 테스트 20 〉	통과 (1022.69ms, 51.3MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0