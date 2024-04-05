frame = []
total = 0
isStrike = isSpare = isDouble = False
for i in range(11):
    while True:
        if i == 10:
            input_score = input("(입력) 보너스 프레임(드로우가 1회일 경우 두 번째 숫자는 0으로 표기하세요) : ")
        else:
            input_score = input("(입력) %d 프레임 : " %(i + 1))
        input_score = input_score.split()

        first, second = int(input_score[0]), int(input_score[1])
        f_total = first + second                # 1회, 2회 쓰러뜨린 핀의 수
        if f_total > 10 and i < 10:
            print("각 프레임 점수의 합계는 10 이하여야 합니다! 다시 입력해주세요.")
            continue
        else:break


    #이전 결과가 스페어 / 스트라이크 / 더블이었을 경우
    if isSpare == True:                     #Spare
        frame[i-1] = list(frame[i-1])         #점수 수정 위해 튜플 -> 리스트
        frame[i-1][3] += first               #점수 갱신
        isSpare = False                     #스페어여부 다시 false로 초기화
        frame[i-1] = tuple(frame[i-1])        #리스트 -> 튜플
        total += first                      #추가한 점수 반영한 총점

    if isDouble == True:                    #Double 
        frame[i-2] = list(frame[i-2])         #'전전' 점수를 변경!
        frame[i-2][3]  += frame[i-1][0] + first
        isDouble = False
        frame[i-2] = tuple(frame[i-2])
        total += first + frame[i-1][0]      #증가량만큼 합산

    if isStrike == True:                    #Strike
        if first == 10 and i != 10:         #1~10 프레임에서 더블이면
            isDouble = True                 #더블여부 true로 설정
        else:
            frame[i-1] = list(frame[i-1])         
            frame[i-1][3] += f_total
            isStrike = False
            frame[i-1] = tuple(frame[i-1])
            total += f_total

    
    if first == 10:                         #Strike
        result = '~'
        isStrike = True                     #스트라이크여부 true로 설정

    elif (first + second) == 10:            #Spare
        result = '/'
        isSpare = True                      #스페어여부 true로 설정

    else:
         result = '-'

    if i != 10:                             #1~10 프레임이면 프레임 기록
        frame.append((first, second, result, f_total))   #보너스 드로우(프레임)은 기록하지 않음.

    if i == 10:                             #보너스 프레임까지 갔을 경우
        print(frame)
        print("Total =", total)             #보너스 프레임의 total은 총점에 합산 X
    else:
        total += f_total                    #1~10 프레임일 경우
        print(frame)
        print("Total =", total)

    if i == 9 and isStrike == False and isSpare == False:   #10프레임에서 스트라이크나 스페어가 아닐 경우
        break                               #그만