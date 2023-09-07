def solution(numbers, hand):
    answer = []
    left = {
        1 : (1, 1),
        4 : (1, 2),
        7 : (1, 3)
    }
    right = {
        3 : (3, 1),
        6 : (3, 2),
        9 : (3, 3)
    }
    middle = {
        2 : (2, 1),
        5 : (2, 2),
        8 : (2, 3),
        0 : (2, 4)
    }
    left_x = 1
    left_y = 4
    right_x = 3
    right_y = 4
    
    
    for number in numbers:
        if number in left:
            answer.append('L')
            left_x, left_y = left[number] 
        elif number in right:
            answer.append('R')
            right_x, right_y = right[number]
        elif number in middle:
            x, y = middle[number]
            left_dts = abs(left_x - x) + abs(left_y - y)
            right_dts = abs(right_x - x) + abs(right_y - y)
            if left_dts > right_dts:
                    answer.append('R')
                    right_x = x
                    right_y = y
            elif left_dts < right_dts:
                answer.append('L')
                left_x = x
                left_y = y
            else :
                answer.append(hand[0].upper())
                if hand == "right":
                    right_x = x
                    right_y = y
                else:
                    left_x = x
                    left_y = y
        
    return ''.join(answer)