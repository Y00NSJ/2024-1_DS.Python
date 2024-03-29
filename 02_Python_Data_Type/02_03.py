def realToFraction(x):     #소수점이 사라질 때까지 곱하기 10
    count = 0        #10을 몇 번 곱했는지 기록 -> 후에 (10^count)가 분모가 됨!

    while True:
        if (x % (10**count)) >= 10:   #나머지가 10보다 큼 = 정수 완성!
            break
        x *= 10      #정수 될 때까지 10배
        count += 1

    gcd = 10 ** count   #최대공약수
    den = 10 ** count
    num = x
    while (x % gcd) != 0:
        x, gcd = gcd, x % gcd

    num = num // gcd
    den = den // gcd

    print(int(num), "/", int(den))

realToFraction(float(input("실수를 입력하세요 : ")))