import math

def calculate_time(ih, im, oh, om):
    dh = (oh - ih) * 60
    dm = om - im
    return dh + dm

def calculate_fee(t, fees):
    if t <= fees[0]:
        return fees[1]
    t1 = fees[0]
    t2 = t - t1
    fee1 = fees[1]
    fee2 = math.ceil(t2 / fees[2]) * fees[3]
    return fee1 + fee2
    

def solution(fees, records):
    p_dict = {}
    t_dict = {}
    f_dict = {}
    
    for record in records:
        t, n, io = record.split(' ')
        if n not in p_dict:
            h, m = map(int, t.split(':'))
            p_dict[n] = [h, m]
        elif n in p_dict and io == 'OUT':
            ih, im = p_dict.pop(n)
            oh, om = map(int, t.split(':'))
            dt = calculate_time(ih, im, oh, om)
            if n not in t_dict:
                t_dict[n] = dt
            else:
                t_dict[n] += dt
    if p_dict:
        for cn in p_dict.keys():
            ih, im = p_dict[cn]
            oh, om = 23, 59
            dt = calculate_time(ih, im, oh, om)
            if cn not in t_dict:
                t_dict[cn] = dt
            else:
                t_dict[cn] += dt
    
    for cn, at in t_dict.items():
        f_dict[cn] = calculate_fee(at, fees)
    
    f_list = sorted(f_dict.items(), key = lambda x : x[0])
    answer = [i[1] for i in f_list]
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 10.5MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.17ms, 10.4MB)
# 테스트 5 〉	통과 (0.32ms, 10.5MB)
# 테스트 6 〉	통과 (0.22ms, 10.5MB)
# 테스트 7 〉	통과 (1.63ms, 10.7MB)
# 테스트 8 〉	통과 (1.04ms, 10.4MB)
# 테스트 9 〉	통과 (0.20ms, 10.4MB)
# 테스트 10 〉	통과 (1.68ms, 10.5MB)
# 테스트 11 〉	통과 (1.99ms, 10.8MB)
# 테스트 12 〉	통과 (3.55ms, 10.8MB)
# 테스트 13 〉	통과 (0.04ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.6MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.4MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0