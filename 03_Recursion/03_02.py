def rmax(lst):
    if len(lst) == 1:               #lst에 원소가 하나만 있다면
        return lst[0]               #max 출력 <escape>
    else:
        if lst[1] >= lst[0]:        #lst[1]이 최댓값이면
            return rmax(lst[1:])    #lst[1:]로 재귀호출
        elif lst[1] < lst[0]:       #lst[0]이 최댓값이면
            lst[1] = lst[0]         #lst[1]을 lst[0]값으로 바꾸고
            return rmax(lst[1:])    #lst[1:]로 재귀호출

def rmin(lst):
    if len(lst) == 1:       
        return lst[0]          
    else:
        if lst[1] <= lst[0]:    
            return rmin(lst[1:])
        elif lst[1] > lst[0]:
            lst[1] = lst[0]
            return rmin(lst[1:])

findList = [3, 1, 6, 5]
print("최댓값 :", rmax(findList), "최솟값 :", rmin(findList))