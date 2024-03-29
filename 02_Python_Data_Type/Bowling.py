score1 = [(8, 0), (4, 3), (8, 2), (4, 6), (2, 6), 
          (10, 0), (9, 0), (10, 0), (8, 2), (10, 0), 
          (10, 10)] # bonus throw


def frame_scores(score):
    game = []
    itotal = 0
    for i in range(10):
        itotal = score[i][0] + score[i][1]

        if itotal == 10:                                #strike / spare
            if score[i][0] == 10:                       #strike(10프레임 포함)
                itotal += score[i+1][0] + score[i+1][1]
                if i < 9 and score[i+1][0] == 10:      #1~9프레임에서 더블
                    itotal += score[i+2][0]
            
            else:
                itotal += score[i+1][0]
        game.append[itotal]
    return game

frame_scores(score1)