sentence = "Van Rossum was born and raised in the Netherlands, \
    where he received a master's degree in mathematics and computer \
        science from the University of Amsterdam in 1982.\
            In December 1989, Van Rossum had been looking for a hobby \
                  programming project that would keep [him] occupied during the week \
                    around Christmas as his office was closed when he decided to write \
                          an interpreter for a new scripting language he had been \
                            thinking about lately: a descendant of ABC that would appeal to Unix/C hackers"

sentence = sentence.lower()
words = sentence.split()
dic = {}
for word in words:
    if word not in dic:
        dic[word] = 0
    dic[word] += 1

print("# of different words =", len(dic))
n = 0
for word, count in dic.items():
    print(word, '(%d)' % count, end = '  ')
    n += 1
    if n % 3 == 0:
        print()