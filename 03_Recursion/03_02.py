def rmax_rmin(lst, idx = 0, maxv = 0, minv = 0):
    if idx == len(lst):     # idx가 lst 최대 인덱스 넘을 경우
        return maxv, minv   # escape
    else:
        if idx == 0:        # 최초
            maxv = minv = lst[0]    #최대최소를 리스트 0번 항목 값으로 set
        if lst[idx] > maxv:         #최대비교
            maxv = lst[idx]
        if lst[idx] < minv:         #최소비교
            minv = lst[idx]
    return rmax_rmin(lst, idx + 1, maxv, minv)      #idx 1 증가해 재귀호출


findList = [50, 2, 100, 120, 1]
maxValue, minValue = rmax_rmin(findList)
print("최댓값 :", maxValue, "\n최솟값 :", minValue)