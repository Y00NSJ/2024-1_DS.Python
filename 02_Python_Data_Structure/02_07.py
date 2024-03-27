scores = [[75, 90, 85], [60, 100, 75], [90, 70, 80]]

for i in scores:
    for j in i:
        if j == i[(len(i)-1)]:
            print(j)
        else:
            print(j, end=",")