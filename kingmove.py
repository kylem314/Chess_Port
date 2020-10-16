exec(open("check.py").read())


def wkingmove(usermove,board,whiteking):

    print("hi")
    wkpossible = []
    wkspaces = []
    whitex = whiteking[0]
    whitey = int(whiteking[1])
    up = 8 - whitey
    down = whitey - 1
    right = 104 - ord(whitex)
    left = ord(whitex) - 97
    if up != 0 and board[whitex + str(whitey+1)][0].lower() != "w":
        wkpossible.append(whitex + str(whitey+1))
        if left != 0 and board[chr(ord(whitex)-1) + str(whitey+1)][0].lower() != "w":
            wkpossible.append(chr(ord(whitex)-1) + str(whitey+1))
        if right != 0 and board[chr(ord(whitex)+1) + str(whitey+1)][0].lower() != "w":
            wkpossible.append(chr(ord(whitex)+1) + str(whitey+1))
    if down != 0 and board[whitex + str(whitey-1)][0].lower() != "w":
        wkpossible.append(whitex + str(whitey-1))
        if left != 0 and board[chr(ord(whitex)-1) + str(whitey-1)][0].lower() != "w":
            wkpossible.append(chr(ord(whitex)-1) + str(whitey-1))
        if right != 0 and board[chr(ord(whitex)+1) + str(whitey-1)][0].lower() != "w":
            wkpossible.append(chr(ord(whitex)+1) + str(whitey-1))
    if left != 0 and board[chr(ord(whitex)-1) + str(whitey)][0].lower() != "w":
        wkpossible.append(chr(ord(whitex)-1) + str(whitey))
    if right != 0 and board[chr(ord(whitex)-1) + str(whitey)][0].lower() != "w":
        wkpossible.append(chr(ord(whitex)+1) + str(whitey))
    print(wkpossible)
    for i in wkpossible:
        print(i)
        piece = board[i]
        if piece[0].lower != "w":
            if whitecheck(usermove,board,i) == False:
                print("why")
                wkspaces.append(i)
    print("what")
    print(wkpossible, "\n", wkspaces)