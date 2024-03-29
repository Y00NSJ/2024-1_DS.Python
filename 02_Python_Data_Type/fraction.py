class Fraction:
    def __init__(self, *x):
        if len(x) == 1:
            dec = x[0]
            frac = self.decimal_fraction(dec)
            self.num = frac.num
            self.den = frac.den
        else:
            self.num = x[0]
            self.den = x[1]

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def gcd(self, a, b):
        while a % b != 0:
            a, b = b, a % b
        return b
    
    def __add__(self, other):
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    
    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        common = self.gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)
    
    def abbreviation(self, a, b):
        common = self.gcd(a, b)
        return Fraction(a//common, b//common)
    
    def decimal_fraction(self, dec):
        count = 0
        while True:
            if dec - int(dec) == 0:
                break
            dec *= 10
            count += 1
        num, den = int(dec), 10**count
        return self.abbreviation(num, den)

num1 = Fraction(3.14)
print(num1)