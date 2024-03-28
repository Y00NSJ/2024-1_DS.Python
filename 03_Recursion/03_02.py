def rmax(lst):
    if len(lst) == 1:       #lst에 원소가 하나만 있다면
        return lst[0]          #max 출력
    else:
        if lst[1] >= lst[0]:    #lst[0] >= max 이면
            rmax(lst[1:])
        elif lst[1] < lst[0]:
            lst[1] = lst[0]
            rmax(lst[1:])



findList = [3, 1, 6, 5]
rmax(findList)