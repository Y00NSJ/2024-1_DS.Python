def rpal(word):
    if len(word) <= 1:      # <escape> 1 = 홀수 palindrome / 0 = 짝수 palindrome
        return True
    else:
        if word[0] != word[-1]: #첫 글자와 끝 글자 다르면
            return False        #탈락
        return rpal(word[1:-1]) #첫 글자와 끝 글자 빼고 재귀호출
    

realOddPal = "abcba"
realEvenPal = "abccba"
notPal = "hello"

print("{} : {} / {} : {} / {} : {}".format(realOddPal, rpal(realOddPal), realEvenPal, rpal(realEvenPal), notPal, rpal(notPal)))
