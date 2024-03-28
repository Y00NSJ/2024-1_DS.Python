def rmax(lst):
    if len(lst) == 0:       #lst에 원소가 없으면
        return max          #max 출력
    else:
        if lst[0] >= max:    #lst[0] >= max 이면
            max = lst[0]          #lst[0]을 max로
        rmax(lst[1:])               #lst[0] 빼고 재귀!

findList = [3, 1, 6, 5]

print(rmax(findList))