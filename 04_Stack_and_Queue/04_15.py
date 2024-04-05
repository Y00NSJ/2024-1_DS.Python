def Palindrome(string):
    stack = []
    for i in range(len(string) // 2):
        stack.push(string[i])
    
    for j in string[len(string)//2:]:
        char = stack.pop()
        if j != char:
            return False
        
for i in range(3):
    str = input(">> ")
    Palindrome(str)