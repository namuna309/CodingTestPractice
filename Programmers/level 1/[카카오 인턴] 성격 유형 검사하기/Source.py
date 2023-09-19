def solution(survey, choices):
    personality_dict = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    personality_list = ['RT', 'CF', 'JM', 'AN']
    answer = ''
    for i in range(len(choices)):
        if choices[i] > 4:
            personality = survey[i][1]
            personality_dict[personality] += choices[i] - 4
        elif choices[i] < 4:
            personality = survey[i][0]
            personality_dict[personality] += 4 - choices[i]
    
    for personality in personality_list:
        if personality_dict[personality[0]] >= personality_dict[personality[1]]:
            answer += personality[0]
        else :
            answer += personality[1]
    
    
    return answer