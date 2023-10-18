def solution(arr1, arr2):

    # 2 3 2   5 4 3
    # 4 2 4   2 4 1
    # 3 1 4   3 1 1
    i1, j1 = len(arr1), len(arr1[0])
    i2, j2 = len(arr2), len(arr2[0])
    nArr = []
    
    for r in range(i1):
        nArr_s = []
        for c in range(j2):
            sum = 0
            arr1_r, arr1_c = r, 0
            arr2_r, arr2_c = 0, c
            while arr1_c < j1 and arr2_r < i2:
                sum += arr1[arr1_r][arr1_c] * arr2[arr2_r][arr2_c]
                arr1_c += 1
                arr2_r += 1
            nArr_s.append(sum)
        nArr.append(nArr_s)
    
    
    return nArr