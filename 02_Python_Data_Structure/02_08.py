#다항식의 튜플화 과정은 구현 생략
p = [(9,4), (5,3), (4,2)]
q = [(7,3), (2,2)]

#def rec_exp(tup1, tup2):

#def term_mul():

def term_add(poly):
    for i in range(1, len(poly)):
        if poly[i][2] == poly[i-1][2]:
            poly[i][1] += poly[i-1][1]
            poly.remove(poly[i-1])
    return poly


def poly_add(p,q):
    result = []
    result = (p+q).sort()       #[(9,4),(7,3),(5,3),(4,2),(2,2)]
    term_add(result)
    return result

def poly_mul(p,q):
    result = []
    for term1 in p:
        for term2 in q:
            term1[0]*=term1[0]
            term1[1]+=term2[1]
            result.add[term1]
    result.sort()
    term_add(result)
    return result


print("P + Q = ", poly_add(p,q))
print("P + Q = ", poly_mul(p,q))