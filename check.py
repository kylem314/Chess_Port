#whiteking = "e1"
#blackking = "e8"
def whitecheck(usermove,board,whiteking):
    #mccabe complexity error, please have mercy on my code
    whitex = whiteking[0]
    whitey = int(whiteking[1])
    up = 8 - whitey
    down = whitey - 1
    right = 104 - ord(whitex)
    left = ord(whitex) - 97
    validmove = 0
    if up == 0:
        if left == 0 or right == 0:
            validmove += 5
        else:
            validmove += 3
    elif down == 0:
        if left == 0 or right == 0:
            validmove += 5
        else:
            validmove += 3
    elif left == 0:
        validmove += 3
    elif right == 0:
        validmove += 3
    #up
    if up != 0:
        squarecheck = 0
        for i in range(1,up+1):
            if board[whitex + str(int(whitey) + i)] != '  ':
                if board[whitex + str(int(whitey) + i)] == "BR" or board[whitex + str(int(whitey) + i)] == "BQ":
                    break
                else:
                    squarecheck = up
                    break
            squarecheck = i
        if squarecheck == up:
            validmove += 1
    #down
    if down != 0:
        squarecheck = 0
        for i in range(1,down+1):
            if board[whitex + str(int(whitey) - i)] != '  ':
                if board[whitex + str(int(whitey) - i)] == "BR" or board[whitex + str(int(whitey) - i)] == "BQ":
                    break
                else:
                    squarecheck = down
                    break
            squarecheck = i
        if squarecheck == down:
            validmove += 1
    #right
    if right != 0:
        squarecheck = 0
        for i in range(1,right+1):
            if board[chr(ord(whitex) + i) + str(whitey)] != '  ':
                if board[chr(ord(whitex) + i) + str(whitey)] == "BR" or board[chr(ord(whitex) + i) + str(whitey)] == "BQ":
                    break
                else:
                    squarecheck = right
                    break
            squarecheck = i
        if squarecheck == right:
            validmove += 1
    #left
    if left != 0:
        squarecheck = 0
        for i in range(1,left+1):
            if board[chr(ord(whitex) - i) + str(whitey)] != '  ':
                if board[chr(ord(whitex) - i) + str(whitey)] == "BR" or board[chr(ord(whitex) - i) + str(whitey)] == "BQ":
                    break
                else:
                    squarecheck = left
                    break
            squarecheck = i
        if squarecheck == left:
            validmove += 1
    #up and to the left
    if up != 0 and left != 0:
        squarecheck = 0
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1,displacement+1):
            if board[chr(ord(whitex) + i) + str(int(whitey) + i)] != '  ':
                if board[chr(ord(whitex) + i) + str(int(whitey) + i)] == 'BB' or board[chr(ord(whitex) + i) + str(int(whitey) + i)] == 'BQ' or i == 1 and board[chr(ord(whitex) + i) + str(int(whitey) + i)] == 'bp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    #down and to the left
    if down != 0 and left != 0:
        squarecheck = 0
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1,displacement+1):
            if board[chr(ord(whitex) + i) + str(int(whitey) - i)] != '  ':
                if board[chr(ord(whitex) + i) + str(int(whitey) - i)] == 'BB' or board[chr(ord(whitex) + i) + str(int(whitey) - i)] == 'BQ' or i == 1 and board[chr(ord(whitex) + i) + str(int(whitey) - i)] == 'bp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    #up and to the right
    if up != 0 and right != 0:
        squarecheck = 0
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1,displacement+1):
            if board[chr(ord(whitex) - i) + str(int(whitey) + i)] != '  ':
                if board[chr(ord(whitex) - i) + str(int(whitey) + i)] == 'BB' or board[chr(ord(whitex) - i) + str(int(whitey) + i)] == 'BQ' or i == 1 and board[chr(ord(whitex) - i) + str(int(whitey) + i)] == 'bp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    #down and to the right
    if down != 0 and right != 0:
        squarecheck = 0
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1,displacement+1):
            if board[chr(ord(whitex) - i) + str(int(whitey) - i)] != '  ':
                if board[chr(ord(whitex) - i) + str(int(whitey) - i)] == 'BB' or board[chr(ord(whitex) - i) + str(int(whitey) - i)] == 'BQ' or i == 1 and board[chr(ord(whitex) - i) + str(int(whitey) - i)] == 'bp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    if validmove == 8:
        return False
    else:
        return True


def blackcheck(usermove,board,blackking):
    #mccabe complexity error, please have mercy on my code
    blackx = blackking[0]
    blacky = int(blackking[1])
    up = 8 - blacky
    down = blacky - 1
    right = 104 - ord(blackx)
    left = ord(blackx) - 97
    validmove = 0
    if up == 0:
        if left == 0 or right == 0:
            validmove += 5
        else:
            validmove += 3
    elif down == 0:
        if left == 0 or right == 0:
            validmove += 5
        else:
            validmove += 3
    elif left == 0:
        validmove += 3
    elif right == 0:
        validmove += 3
    #up
    if up != 0:
        squarecheck = 0
        for i in range(1,up+1):
            if board[blackx + str(int(blacky) + i)] != '  ':
                if board[blackx + str(int(blacky) + i)] == "WR" or board[blackx + str(int(blacky) + i)] == "WQ":
                    break
                else:
                    squarecheck = up
                    break
            squarecheck = i
        if squarecheck == up:
            validmove += 1
    #down
    if down != 0:
        squarecheck = 0
        for i in range(1,down+1):
            if board[blackx + str(int(blacky) - i)] != '  ':
                if board[blackx + str(int(blacky) - i)] == "WR" or board[blackx + str(int(blacky) - i)] == "WQ":
                    break
                else:
                    squarecheck = down
                    break
            squarecheck = i
        if squarecheck == down:
            validmove += 1
    #right
    if right != 0:
        squarecheck = 0
        for i in range(1,right+1):
            if board[chr(ord(blackx) + i) + str(blacky)] != '  ':
                if board[chr(ord(blackx) + i) + str(blacky)] == "WR" or board[chr(ord(blackx) + i) + str(blacky)] == "WQ":
                    break
                else:
                    squarecheck = right
                    break
            squarecheck = i
        if squarecheck == right:
            validmove += 1
    #left
    if left != 0:
        squarecheck = 0
        for i in range(1,left+1):
            if board[chr(ord(blackx) - i) + str(blacky)] != '  ':
                if board[chr(ord(blackx) - i) + str(blacky)] == "WR" or board[chr(ord(blackx) - i) + str(blacky)] == "WQ":
                    break
                else:
                    squarecheck = left
                    break
            squarecheck = i
        if squarecheck == left:
            validmove += 1
    #up and to the left
    if up != 0 and left != 0:
        squarecheck = 0
        if up > left:
            displacement = left
        elif up < left:
            displacement = up
        else:
            displacement = left
        for i in range(1,displacement+1):
            if board[chr(ord(blackx) + i) + str(int(blacky) + i)] != '  ':
                if board[chr(ord(blackx) + i) + str(int(blacky) + i)] == 'WB' or board[chr(ord(blackx) + i) + str(int(blacky) + i)] == 'WQ' or i == 1 and board[chr(ord(blackx) + i) + str(int(blacky) + i)] == 'wp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    #down and to the left
    if down != 0 and left != 0:
        squarecheck = 0
        if down > left:
            displacement = left
        elif down < left:
            displacement = down
        else:
            displacement = left
        for i in range(1,displacement+1):
            if board[chr(ord(blackx) + i) + str(int(blacky) - i)] != '  ':
                if board[chr(ord(blackx) + i) + str(int(blacky) - i)] == 'WB' or board[chr(ord(blackx) + i) + str(int(blacky) - i)] == 'WQ' or i == 1 and board[chr(ord(blackx) + i) + str(int(blacky) - i)] == 'wp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    #up and to the right
    if up != 0 and right != 0:
        if up > right:
            displacement = right
        elif up < right:
            displacement = up
        else:
            displacement = right
        for i in range(1,displacement+1):
            if board[chr(ord(blackx) - i) + str(int(blacky) + i)] != '  ':
                if board[chr(ord(blackx) - i) + str(int(blacky) + i)] == 'WB' or board[chr(ord(blackx) - i) + str(int(blacky) + i)] == 'WQ' or i == 1 and board[chr(ord(blackx) - i) + str(int(blacky) + i)] == 'wp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    #down and to the right
    if down != 0 and right != 0:
        if down > right:
            displacement = right
        elif down < right:
            displacement = down
        else:
            displacement = right
        for i in range(1,displacement+1):
            if board[chr(ord(blackx) - i) + str(int(blacky) - i)] != '  ':
                if board[chr(ord(blackx) - i) + str(int(blacky) - i)] == 'WB' or board[chr(ord(blackx) - i) + str(int(blacky) - i)] == 'WQ' or i == 1 and board[chr(ord(blackx) - i) + str(int(blacky) - i)] == 'wp':
                    break
                else:
                    squarecheck = displacement
                    break
            squarecheck = i
        if squarecheck == displacement:
            validmove += 1
    '''
    #knights
    if up > 0:
      if up > 1:
        if right > 0:
          if right > 1:
            #right up
          #up left
        else:
          validmove += 1
        if left > 0:
          if left > 1:
            #right up
          #up right
        else:
          validmove += 1
    '''
    if validmove == 8:
        return False
    else:
        return True