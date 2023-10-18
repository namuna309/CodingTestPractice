from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_list.append(str1[i]+ str1[i + 1])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_list.append(str2[i]+ str2[i + 1])
                
    str1_cnt = Counter(str1_list)
    str2_cnt = Counter(str2_list)
    
    inter = list((str1_cnt & str2_cnt).elements())
    union = list((str1_cnt | str2_cnt).elements())
    
    if len(inter) == len(union) == 0:
        return 65536
    else:
        return int(65536 * len(inter) / len(union))