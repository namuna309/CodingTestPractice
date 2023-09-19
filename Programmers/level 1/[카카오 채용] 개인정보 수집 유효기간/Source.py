from datetime import datetime

def calculate_date(privacy_date, privacy_term, terms_dict):
    year = privacy_date[0]
    month = privacy_date[1]
    day = privacy_date[2]
    
    month += (day + terms_dict[privacy_term]) // 28
    day = (day + terms_dict[privacy_term]) % 28 - 1
    
    
    if day <= 0:
        day += 28
        month -= 1
    print(month)
    while month > 12:
        year += month // 12
        month = month % 12
    
    if month <= 0 :
        month += 12
        year -= 1
    
    return [year, month, day]
    

def solution(today, terms, privacies):
    today_split = [int(i) for i in today.split('.')]
    terms = [i.split(' ') for i in terms]
    terms_dict = {i[0]: int(i[-1]) * 28 for i in terms}
    privacies = [i.split(' ') for i in privacies]
    privacies_split = [[list(map(int, i[0].split('.'))), i[-1]] for i in privacies]
    answer = []
    
    for i in range(len(privacies)):
        privacy_date = privacies_split[i][0]
        privacy_term = privacies_split[i][1]
        expire_date_split = calculate_date(privacy_date, privacy_term, terms_dict)
        expire_date = datetime(expire_date_split[0], expire_date_split[1], expire_date_split[2])
        today = datetime(today_split[0], today_split[1], today_split[2])
        print(today, expire_date)
        if expire_date < today:
            answer.append(i + 1)
    
    return answer