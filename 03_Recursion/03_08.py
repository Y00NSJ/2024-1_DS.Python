def rharm(n):
    if n == 1:
        return 1
    else:
        return rharm(n-1) + (1/n)

print("H_2 = 1/1 + 1/2 = 3/2 = 15/10 =", rharm(2))
