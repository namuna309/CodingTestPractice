from collections import Counter
from itertools import combinations

def solution(orders, course):
    order_str = ''
    new_menu = []
    can_menu_dict = {}
    for i in course :
        ft_menu = []
        for order in orders:
            for menu in combinations(order, i):
                ft_menu.append(''.join(sorted(menu)))
        can_menu = Counter(ft_menu).most_common()
        new_menu += [menu for menu, cnt in can_menu if cnt > 1 and cnt == can_menu[0][1]]

    return sorted(new_menu)

# 정확성  테스트
# 테스트 1 〉	통과 (0.12ms, 10.3MB)
# 테스트 2 〉	통과 (0.08ms, 10.2MB)
# 테스트 3 〉	통과 (0.12ms, 10.1MB)
# 테스트 4 〉	통과 (0.12ms, 10.2MB)
# 테스트 5 〉	통과 (0.12ms, 10.3MB)
# 테스트 6 〉	통과 (0.48ms, 10.2MB)
# 테스트 7 〉	통과 (0.29ms, 10.2MB)
# 테스트 8 〉	통과 (5.33ms, 10.4MB)
# 테스트 9 〉	통과 (1.83ms, 10.3MB)
# 테스트 10 〉	통과 (2.43ms, 10.6MB)
# 테스트 11 〉	통과 (1.29ms, 10.4MB)
# 테스트 12 〉	통과 (1.57ms, 10.4MB)
# 테스트 13 〉	통과 (2.37ms, 10.6MB)
# 테스트 14 〉	통과 (2.55ms, 10.4MB)
# 테스트 15 〉	통과 (2.37ms, 10.5MB)
# 테스트 16 〉	통과 (0.63ms, 10.4MB)
# 테스트 17 〉	통과 (0.41ms, 10.3MB)
# 테스트 18 〉	통과 (0.25ms, 10.1MB)
# 테스트 19 〉	통과 (0.04ms, 10.2MB)
# 테스트 20 〉	통과 (0.42ms, 10.1MB)
# 
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0