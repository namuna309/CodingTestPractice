def print_hotel(hotel) :
    print(len(hotel))
    for i in range(len(hotel)):
        for j in range(len(hotel[0])):
            print(i, j, hotel[i][j])

def solution(book_time):
    hotel = []
#   1. 1분 단위로 사용 여부를 기록하는 배열을 만든다
#   2. 해당시간에 사용자가 있거나 방이 없으면 방을 추가한다
#   3. 주어진 시간을 통해 방에 사용 여부를 기록한다
    for nbt in range(len(book_time)):
        
        start_bt = book_time[nbt][0]
        start_bt_h, start_bt_m = map(int, start_bt.split(':'))
        end_bt = book_time[nbt][1]
        end_bt_h, end_bt_m = map(int, end_bt.split(':'))
        end_bt_m += 10
        if end_bt_m >= 60:
            if end_bt_h == 23:
                end_bt_m = 59
            else:
                end_bt_m = (end_bt_m + 10) % 60
                end_bt_h += 1            

        if start_bt_h == end_bt_h:
            if len(hotel) == 0:
                hotel.append([[False] * 60 for i in range(24)])
            for i in range(len(hotel)):
                newone = False
                for m in range(start_bt_m, end_bt_m):
                    if hotel[i][start_bt_h][m]:
                        newone = True
                        break
                if newone and i < len(hotel) - 1:
                    continue
                if newone:
                    hotel.append([[False] * 60 for i in range(24)])
                for mm in range(start_bt_m, end_bt_m):
                    hotel[-1][start_bt_h][mm] = True
                break
        else:
            if len(hotel) == 0:
                hotel.append([[False] * 60 for i in range(24)])
            for i in range(len(hotel)):
                newone = False
                for h in range(start_bt_h, end_bt_h + 1):
                    if h == start_bt_h:
                        for m in range(start_bt_m, 60):
                            if hotel[i][h][m]:
                                newone = True
                                break
                    elif h == end_bt_h:
                        for m in range(end_bt_m):
                            if hotel[i][h][m]:
                                newone = True
                                break
                    else:
                        for m in range(60):
                            if hotel[i][h][m]:
                                newone = True
                                break
                if newone and i < len(hotel) - 1:
                    continue
                elif newone:
                    hotel.append([[False] * 60 for i in range(24)])
                for h in range(start_bt_h, end_bt_h + 1):
                    if h == start_bt_h:
                        for m in range(start_bt_m, 60):
                            hotel[-1][h][m] = True
                    elif h == end_bt_h:
                        for m in range(end_bt_m):
                            hotel[-1][h][m] = True
                    else:
                        for m in range(60):
                            hotel[-1][h][m] = True
                break
                 
    return len(hotel)

# 정확성  테스트
# 테스트 1 〉	실패 (0.14ms, 10.5MB)
# 테스트 2 〉	실패 (66.58ms, 11.4MB)
# 테스트 3 〉	실패 (1105.10ms, 15.6MB)
# 테스트 4 〉	실패 (234.09ms, 12.7MB)
# 테스트 5 〉	통과 (0.17ms, 10.4MB)
# 테스트 6 〉	실패 (727.67ms, 14.4MB)
# 테스트 7 〉	실패 (1092.57ms, 14.8MB)
# 테스트 8 〉	실패 (213.66ms, 12.4MB)
# 테스트 9 〉	실패 (64.15ms, 11.3MB)
# 테스트 10 〉	실패 (518.47ms, 13.3MB)
# 테스트 11 〉	실패 (1388.51ms, 15.8MB)
# 테스트 12 〉	실패 (1244.28ms, 15.4MB)
# 테스트 13 〉	실패 (32.13ms, 11.1MB)
# 테스트 14 〉	실패 (580.06ms, 15.1MB)
# 테스트 15 〉	실패 (473.24ms, 15MB)
# 테스트 16 〉	실패 (124.70ms, 12.4MB)
# 테스트 17 〉	실패 (633.72ms, 15.2MB)
# 테스트 18 〉	실패 (416.65ms, 14.2MB)
# 테스트 19 〉	통과 (511.52ms, 23.8MB)
# 
# 채점 결과
# 정확성: 10.5
# 합계: 10.5 / 100.0