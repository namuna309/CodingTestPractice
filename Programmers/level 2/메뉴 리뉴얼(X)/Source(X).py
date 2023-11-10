from collections import Counter
from itertools import combinations

def solution(orders, course):
    order_str = ''
    new_menu = []
    for order in orders:
        order_str += order
    
    od = Counter(order_str)

    fm = []
    for menu, c in od.items():
        if c > 1:
            fm.append(menu)
    
    for i in range(len(course)):
        sub_menus = list(combinations(fm, course[i]))
        mc = {}
        for sub_menu in sub_menus:
            s_menu = ''.join(sub_menu)
            mc[s_menu] = 0
            for order in orders:
                in_menu = True
                for sm in sub_menu:
                    if sm not in order:
                        in_menu = False
                        break
                if in_menu:
                    mc[s_menu] += 1     
            
        if len(mc) > 0:
            mmc = max(mc.values())

            for m, c in mc.items():
                if mmc >= 2 and c == mmc:
                    new_menu.append(''.join(sorted(m)))
    new_menu.sort()

    return new_menu

# 정확성  테스트
# 테스트 1 〉	통과 (0.12ms, 10.2MB)
# 테스트 2 〉	통과 (0.08ms, 10.1MB)
# 테스트 3 〉	통과 (0.13ms, 10.4MB)
# 테스트 4 〉	통과 (0.15ms, 10.2MB)
# 테스트 5 〉	통과 (0.31ms, 10.2MB)
# 테스트 6 〉	통과 (0.56ms, 10.2MB)
# 테스트 7 〉	통과 (0.57ms, 10.2MB)
# 테스트 8 〉	통과 (3.44ms, 10.2MB)
# 테스트 9 〉	통과 (4.79ms, 10.3MB)
# 테스트 10 〉	통과 (143.16ms, 21.2MB)
# 테스트 11 〉	통과 (117.16ms, 21MB)
# 테스트 12 〉	통과 (146.42ms, 21.3MB)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	실패 (시간 초과)
# 테스트 15 〉	통과 (9478.76ms, 826MB)
# 테스트 16 〉	통과 (4.60ms, 10.5MB)
# 테스트 17 〉	통과 (43.46ms, 12MB)
# 테스트 18 〉	통과 (23.15ms, 11.5MB)
# 테스트 19 〉	통과 (0.24ms, 10.2MB)
# 테스트 20 〉	통과 (2.84ms, 10.4MB)
# 
# 채점 결과
# 정확성: 90.0
# 합계: 90.0 / 100.0