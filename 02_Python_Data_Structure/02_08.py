#다항식의 튜플화 과정은 구현 생략
p = [(9,4), (5,3), (4,2)]
q = [(7,3), (2,2)]

#def rec_exp(tup1, tup2):

#def term_mul():


def term_add(poly):
    tlist = [] #연산 결과 리스트
    for i in range(1, len(poly)):
        if poly[i][1] == poly[i-1][1]:  #지수가 같으면
            tlist.append((poly[i][0] + poly[i-1][0], poly[i][1])) #계수덧셈
            poly[i] = (0, 0) #리스트 중복추가 방지
            i += 1 #점프
        else:
            if poly[i-1] == (0, 0): #리스트 중복추가 방지
                continue
            else:
                 tlist.append((poly[i-1][0], poly[i-1][1])) #동차수항 없으면 바로 추가
    return tlist


def poly_add(p,q):
    result = p+q
    result.sort()       #[(9,4),(7,3),(5,3),(4,2),(2,2)]
    result.reverse()    #내림차순 정렬하기
    
    return term_add(result)


def poly_mul(p,q):
    result = []

    for i in range(0,len(p)):
        for j in range(0,len(q)):
            result.append((p[i][0]*q[j][0], p[i][1]+q[j][1]))

    result.sort()
    print(result)
    result.reverse()
    print(result)
    #term_add(result)
    #return result

print("P + Q = ", poly_add(p,q))
poly_mul(p,q)
#print("P * Q = ", poly_mul(p,q))