sparsematrix = [[0, 3, 0, 2], [8, 0, 4, 0], [0, 0, 0, 5]]

def realnum(spm):
    row = len(spm)
    col = len(spm[0])
    count = 0
    result = []
    for i in range(row):
        for j in range(col):
            if spm[i][j] != 0:
                result.append((i, j, spm[i][j]))
                count += 1
    result.insert(0, (row, col, count))
    return result

def ltom(lst):
    matrix = []
    for row in range(lst[0][0]):
        mrow = []
        for col in range(lst[0][1]):
            mrow.append(0)
        matrix.append(mrow)
    
    for i in range(1, len(lst)):
        matrix[lst[i][0]][lst[i][1]] = lst[i][2]
    
    for rrow in matrix:
        for rcol in rrow:
            print(rcol, end = ' ')
        print()



lst = realnum(sparsematrix)
print(lst)
ltom(lst)
