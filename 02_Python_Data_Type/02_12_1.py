score1 = [(8, 0), (4, 3), (8, 2), (4, 6), (2, 6), 
          (10, 0), (9, 0), (10, 0), (8, 2), (10, 0), 
          (10, 10)] # bonus throw
score2 = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), 
          (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), 
          (10, 10)] # bonus throw
score_list = [score1, score2]

for score in score_list:
    i = total = 0
    frame = []
    for first, second in score:
        f_total = first + second
        next_first, next_second = score[i+1]
        if first == 10:                         #Strike
            result = 'STRIKE'
            f_total += next_first + next_second #1~9 프레임에서 더블
            if i != 9 and next_first == 10:
                next_next_first, next_next_second = score[i+2]
                f_total += next_next_first
        elif (first + second) == 10:            #Spare
            result = 'SPARE'
            f_total += next_first
        else:
            result = 'NONE'
        
        total += f_total
        frame.append((f_total, result))
        i += 1
        if i == 10:                             #보너스 프레임 제외
            break

print(frame)
print("Total = ", total)
print()