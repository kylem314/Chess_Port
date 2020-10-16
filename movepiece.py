def kingPos(wkp,bkp):
    global checkmate
    WK = 'WK' in board.values()
    BK = 'BK' in board.values()#if the king is in = true

    if WK != True: #WK is no longer on the board
        print("black wins ",end="")
        endAni(colors[whitecolor], colors[blackcolor], board[wkp])
        print("\nBlack wins. GG\nGame Key: ", Key, "\nSave this key to be able to view a replay of your game\n\n", end = "")
        blackpersp(whitecolor,blackcolor)
        checkmate = True
        return "","" #work around
    elif BK != True: #BK is no longer on the board
        print("white  wins ",end="")
        endAni(colors[blackcolor], colors[whitecolor], board[bkp])
        print("\nWhite wins. GG\nGame Key: ", Key, "\nSave this key to be able to view a replay of your game\n\n", end = "")
        whitepersp(whitecolor,blackcolor)
        checkmate = True
        return "","" #work around
    else:
        print("everyone is still alive")
        for k,v in board.items():
            if v == "WK":
                whitekingposition = k #key of the value
                break

        for k,z in board.items():
            if z == "BK":
                blackkingposition = k #key of the value
                break

        #return whitekingposition,blackkingposition
        return whitekingposition,blackkingposition
from animation import *
#exec(open("check.py").read())
def piecemove(piece, usermove, whitemove):
    exec(open("piecemove.py").read())
#replaying = False
global turnrecorded
while checkmate == False:
    usermove = input("What move would you like to make? (startsquare endsquare to move a piece, resign to resign the game)\n") #this prompts for user input
    capturing = False
    moveable = False
    turnrecorded = False
    if usermove.lower() == "resign":
        if whitemove == False and turnnumber != 1:
            if replaying == False:
                savefile = open("savenotation.txt", "a")
                savefile.write(turnnumberlist[turnnumber - 1] + ". " + whitemovelist[turnnumber - 1] + "\n" + "Black resigned" + "\n")
                savefile.close()
                savefile = open("savereplay.txt", "a")
                savefile.write("#W   ")
                savefile.close()
            print("\nWhite wins. GG\nGame Key: ", Key, "\nSave this key to be able to view a replay of your game\n\n", end = "")
            whitepersp(whitecolor,blackcolor)
            break
        elif whitemove == False and turnnumber <= 1:
            if replaying == False:
                savefile = open("savenotation.txt", "a")
                savefile.write("\n" + turnnumberlist[turnnumber] + ". " + whitemovelist[turnnumber] + "\n" + "Black resigned" + "\n")
                savefile.close()
                savefile = open("savereplay.txt", "a")
                savefile.write("#W   ")
                savefile.close()
            print("\nWhite wins. GG\nGame Key: ", Key, "\nSave this key to be able to view a replay of your game\n\n", end = "")
            whitepersp(whitecolor,blackcolor)
            break
        else:
            if replaying == False:
                savefile = open("savenotation.txt", "a")
                savefile.write("White resigned" + "\n")
                savefile.close()
                savefile = open("savereplay.txt", "a")
                savefile.write("#B   ")
            print("\nBlack wins. GG\nGame Key: ", Key, "\nSave this key to be able to view a replay of your game\n\n", end = "")
            blackpersp(whitecolor,blackcolor)
            break
        moveable = False
    elif usermove == "0-0" or usermove == "0-0  ":
        usermove == "0-0  "
        if whitemove == True and wkcastle == True:
            #insert collision mechanics to check 4,3,3 directions for e1, f1, and g1 to see if king is in check
            if board["f1"] == '  ' and board["g1"] == '  ':# and whitecheck(usermove,board,"e1") == False and whitecheck(usermove,board,"f1") == False and whitecheck(usermove,board,"g1") == False:
                wkcastle = False
                wqcastle = False
                board["e1"] = '  '
                board["f1"] = 'WR'
                board["g1"] = 'WK'
                board["h1"] = '  '
                moveable = True#ED6A58
                turnrecorded = True
                whitemovelist.append("0-0    ")
                if replaying == False:
                    savefile = open("savereplay.txt", "a")
                    savefile.write("0-0W ")
                    savefile.close()
        elif whitemove == False and bkcastle == True:
            if board["f8"] == '  ' and board["g8"] == '  ':# and blackcheck(usermove,board,"e8") == False and blackcheck(usermove,board,"f8") == False and blackcheck(usermove,board,"g8") == False:
                bkcastle = False
                bqcastle = False
                board["e8"] = '  '
                board["f8"] = 'BR'
                board["g8"] = 'BK'
                board["h8"] = '  '
                moveable = True
                turnrecorded = True
                blackmovelist.append("0-0    ")
                if replaying == False:
                    savefile = open("savereplay.txt", "a")
                    savefile.write("0-0B ")
                    savefile.close()
            #same for this
    #queenside castle
    elif usermove == "0-0-0":
        if whitemove == True and wqcastle == True:
            if board["b1"] == '  ' and board["c1"] == '  ' and board["d1"] == '  ':# and whitecheck(usermove,board,"e1") == False and whitecheck(usermove,board,"d1") == False and whitecheck(usermove,board,"c1") == False and whitecheck(usermove,board,"b1"):
                wkcastle = False
                wqcastle = False
                board["a1"] = '  '
                board["b1"] = '  '
                board["c1"] = 'WK'
                board["d1"] = 'WR'
                board["e1"] = '  '
                moveable = True
                turnrecorded = True
                whitemovelist.append("0-0-0  ")
                if replaying == False:
                    savefile = open("savereplay.txt", "a")
                    savefile.write("0-0-W")
                    savefile.close()
            #insert collision mechanics to check 4,3,3 directions for e1, f1, and g1 to see if king is in check
        elif whitemove == False and bqcastle == True:
            if board["b8"] == '  ' and board["c8"] == '  ' and board["d8"] == '  ':# and whitecheck(usermove,board,"e8") == False and whitecheck(usermove,board,"d8") == False and whitecheck(usermove,board,"c8") == False and whitecheck(usermove,board,"b8"):
                bkcastle = False
                bqcastle = False
                board["a8"] = '  '
                board["b8"] = '  '
                board["c8"] = 'BK'
                board["d8"] = 'BR'
                board["e8"] = '  '
                moveable = True
                turnrecorded = True
                blackmovelist.append("0-0-0  ")
                if replaying == False:
                    savefile = open("savereplay.txt", "a")
                    savefile.write("0-0-B")
                    savefile.close()
    else:
        try:
            if len(usermove) == 5 and usermove[2] == " " and usermove[0].islower() == True and usermove[3].islower() == True and ord(usermove[0]) - 96 <= 8 and ord(usermove[3]) - 96 <= 8 and int(usermove[1]) <= 8 and int(usermove[4]) <= 8:
                piece = str(board[usermove[0:2]])
                targetspace = str(board[usermove[3:5]])
                piececolor = piece[0]
                movingpiece = piece[1]
                #checks if valid chess move
                if whitemove == True and piececolor == "W" and targetspace[0].lower() != "w" or whitemove == False and piececolor == "B" and targetspace[0].lower() != "b":
                    #knight: x displacement = 2 and y displacement = 1, or vice versa
                    if movingpiece == "N":
                        if abs(ord(usermove[0]) - ord(usermove[3])) == 2 and abs(int(usermove[1]) - int(usermove[4])) == 1 or abs(ord(usermove[0]) - ord(usermove[3])) == 1 and abs(int(usermove[1]) - int(usermove[4])) == 2:
                            moveable = True
                            piecemove(piece,usermove,whitemove)
                    #rook: x displacement = 0 or y displacement = 0
                    elif movingpiece == "R":
                        if abs(ord(usermove[0]) - ord(usermove[3])) == 0 and usermove[0:2] != usermove[3:5] or abs(int(usermove[1]) - int(usermove[4])) == 0 and usermove[0:2] != usermove[3:5]:
                            squarecheck = 0
                            if abs(int(usermove[1]) - int(usermove[4])) == 1 or abs(ord(usermove[0]) - ord(usermove[3])) == 1:
                                if usermove[3:5] == "a1" and wqcastle == True:
                                    wqcastle = False
                                elif usermove[3:5] == "h1" and wkcastle == True:
                                    wkcastle = False
                                elif usermove[3:5] == "a8" and bqcastle == True:
                                    bqcastle = False
                                elif usermove[3:5] == "h8" and bkcastle == True:
                                    bkcastle = False
                                moveable = True
                                piecemove(piece,usermove,whitemove)
                            elif abs(ord(usermove[0]) - ord(usermove[3])) == 0:
                                displacement = int(usermove[4]) - int(usermove[1])
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[usermove[0] + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        if usermove[3:5] == "a1" and wqcastle == True:
                                            wqcastle = False
                                        elif usermove[3:5] == "h1" and wkcastle == True:
                                            wkcastle = False
                                        elif usermove[3:5] == "a8" and bqcastle == True:
                                            bqcastle = False
                                        elif usermove[3:5] == "h8" and bkcastle == True:
                                            bkcastle = False
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[usermove[0] + str(int(usermove[1]) + i)] != "  ":
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        if usermove[3:5] == "a1" and wqcastle == True:
                                            wqcastle = False
                                        elif usermove[3:5] == "h1" and wkcastle == True:
                                            wkcastle = False
                                        elif usermove[3:5] == "a8" and bqcastle == True:
                                            bqcastle = False
                                        elif usermove[3:5] == "h8" and bkcastle == True:
                                            bkcastle = False
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                            elif abs(int(usermove[4]) - int(usermove[1])) == 0:
                                displacement = ord(usermove[3]) - ord(usermove[0])
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[chr(ord(usermove[0]) + i) + str(usermove[1])] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        if usermove[3:5] == "a1" and wqcastle == True:
                                            wqcastle = False
                                        elif usermove[3:5] == "h1" and wkcastle == True:
                                            wkcastle = False
                                        elif usermove[3:5] == "a8" and bqcastle == True:
                                            bqcastle = False
                                        elif usermove[3:5] == "h8" and bkcastle == True:
                                            bkcastle = False
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[chr(ord(usermove[0]) + i) + str(usermove[1])] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        if usermove[3:5] == "a1" and wqcastle == True:
                                            wqcastle = False
                                        elif usermove[3:5] == "h1" and wkcastle == True:
                                            wkcastle = False
                                        elif usermove[3:5] == "a8" and bqcastle == True:
                                            bqcastle = False
                                        elif usermove[3:5] == "h8" and bkcastle == True:
                                            bkcastle = False
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                    #bishop: x displacement = y displacement and starting != beginning
                    elif movingpiece == "B":
                        if abs(ord(usermove[0]) - ord(usermove[3])) == abs(int(usermove[1]) - int(usermove[4])) and usermove[0:2] != usermove[3:5]:
                            squarecheck = 0
                            absdisplacement = abs(int(usermove[4]) - int(usermove[1]))
                            displacement = int(usermove[4]) - int(usermove[1])
                            if abs(int(usermove[1]) - int(usermove[4])) == 1 and abs(ord(usermove[0]) - ord(usermove[3])) == 1:
                                moveable = True
                                piecemove(piece,usermove,whitemove)
                            elif ord(usermove[3]) - ord(usermove[0]) > 0:
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[chr(ord(usermove[0]) + i) + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[chr(ord(usermove[0]) - i) + str(int(usermove[1]) + i)] != "  ":
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                            elif ord(usermove[3]) - ord(usermove[0]) < 0:
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[chr(ord(usermove[0]) - i) + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[chr(ord(usermove[0]) + i) + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                    #queen: x disp = y disp, or x disp = 0, or y disp = 0 (bishop combined with rook)
                    elif movingpiece == "Q":
                        if abs(ord(usermove[0]) - ord(usermove[3])) == abs(int(usermove[1]) - int(usermove[4])) and usermove[0:2] != usermove[3:5] or abs(ord(usermove[0]) - ord(usermove[3])) == 0 or abs(int(usermove[1]) - int(usermove[4])) == 0:
                            squarecheck = 0
                            absdisplacement = abs(int(usermove[4]) - int(usermove[1]))
                            displacement = int(usermove[4]) - int(usermove[1])
                            if abs(int(usermove[1]) - int(usermove[4])) == 1 or abs(ord(usermove[0]) - ord(usermove[3])) == 1:
                                moveable = True
                                piecemove(piece,usermove,whitemove)
                            elif abs(ord(usermove[0]) - ord(usermove[3])) == 0:
                                displacement = int(usermove[4]) - int(usermove[1])
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[usermove[0] + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[usermove[0] + str(int(usermove[1]) + i)] != "  ":
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                            elif abs(int(usermove[4]) - int(usermove[1])) == 0:
                                displacement = ord(usermove[3]) - ord(usermove[0])
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[chr(ord(usermove[0]) + i) + str(usermove[1])] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[chr(ord(usermove[0]) + i) + str(usermove[1])] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                            elif ord(usermove[3]) - ord(usermove[0]) > 0:
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[chr(ord(usermove[0]) + i) + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[chr(ord(usermove[0]) - i) + str(int(usermove[1]) + i)] != "  ":
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                            elif ord(usermove[3]) - ord(usermove[0]) < 0:
                                if displacement > 0:
                                    for i in range(1,displacement):
                                        if board[chr(ord(usermove[0]) - i) + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == displacement-1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                                elif displacement < 0:
                                    for i in range(displacement+1,0):
                                        if board[chr(ord(usermove[0]) + i) + str(int(usermove[1]) + i)] != '  ':
                                            break
                                        squarecheck = i
                                    if squarecheck == -1:
                                        moveable = True
                                        piecemove(piece,usermove,whitemove)
                    #king: x disp = y disp = 1, or xdisp + y disp = 1
                    elif movingpiece == "K":
                        if abs(ord(usermove[0]) - ord(usermove[3])) == abs(int(usermove[1]) - int(usermove[4])) == 1 or abs(ord(usermove[0]) - ord(usermove[3])) + abs(int(usermove[1]) - int(usermove[4])) == 1:
                            if whitemove == True:
                                wkcastle = False
                                wqcastle = False
                            else:
                                bkcastle = False
                                bqcastle = False
                            moveable = True
                            piecemove(piece,usermove,whitemove)
                #pawnmove
                elif whitemove == True and piececolor == "w" and targetspace[0].lower() != "w":
                    if usermove[4] != 1:
                        wpawninbetween = board[str(usermove[3]) + str(int(usermove[4])-1)]
                    #moving pawn forward normally
                    if ord(usermove[0]) - ord(usermove[3]) == 0:
                        #checks one space
                        if int(usermove[4]) - int(usermove[1]) == 1:
                            if targetspace == '  ':
                                moveable = True
                                piecemove(piece,usermove,whitemove)
                                if usermove[4] != "8":
                                    turnrecorded = True
                                    whitemovelist.append(usermove[3:5] + "     ")
                                # Promotion
                                elif usermove[4] == "8":
                                    turnrecorded = True
                                    promochoice = input("What would you like to promote to?\nKnight, Bishop, Rook, or Queen.\n")
                                    for key,value in promoptions.items():
                                        if promochoice.title() == key:
                                            board[usermove[3:5]] = "W" + value
                                            whitemovelist.append(usermove[3:5] + "=" + value + "   ")
                                            savefile = open("savereplay.txt", "a")
                                            savefile.write(usermove[0:2] + value + usermove[3:5])
                                            savefile.close()
                                            promoted = True
                                            #pawnPromo(colors[whitecolor],promochoice.title())#
                        #or two spaces
                        elif int(usermove[4]) - int(usermove[1]) == 2 and int(usermove[1]) == 2:
                            if targetspace == '  ' and wpawninbetween == '  ':
                                moveable = True
                                piecemove(piece,usermove,whitemove)
                                if moveable == True:
                                    turnrecorded = True
                                    whitemovelist.append(usermove[3:5] + "     ")
                    #capturing
                    if targetspace[0].lower() == "b":
                        if abs(ord(usermove[0]) - ord(usermove[3])) == int(usermove[4]) - int(usermove[1]) == 1:
                            moveable = True
                            piecemove(piece,usermove,whitemove)
                            if moveable == True:
                                turnrecorded = True
                                if usermove[4] != "8":
                                    turnrecorded = True
                                    whitemovelist.append(usermove[0] + "x" + usermove[3:5] + "   ")
                                # Promotion
                                elif usermove[4] == "8":
                                    turnrecorded = True
                                    promochoice = input("What would you like to promote to?\nKnight, Bishop, Rook, or Queen.\n")
                                    for key,value in promoptions.items():
                                        if promochoice.title() == key:
                                            board[usermove[3:5]] = "W" + value
                                            whitemovelist.append(usermove[0] + "x" + usermove[3:5] + "=" + value + " ")
                                            savefile = open("savereplay.txt", "a")
                                            savefile.write(usermove[0:2] + value + usermove[3:5])
                                            savefile.close()
                                            promoted = True
                                            #pawnPromo(colors[whitecolor],promochoice.title())
                #black pawnmove
                elif whitemove == False and piececolor == "b" and targetspace[0].lower() != "b":
                    if usermove[4] != 8:
                        bpawninbetween = board[str(usermove[3]) + str(int(usermove[4])+1)]
                    #black pawn normally
                    if ord(usermove[0]) - ord(usermove[3]) == 0:
                        #checks one space
                        if int(usermove[1]) - int(usermove[4]) == 1:
                            if targetspace == '  ':
                                moveable = True
                                piecemove(piece,usermove,whitemove)
                                if usermove[4] != "1":
                                    turnrecorded = True
                                    blackmovelist.append(usermove[3:5] + "     ")
                                # Promotion
                                elif usermove[4] == "1":
                                    turnrecorded = True
                                    promochoice = input("What would you like to promote to?\nKnight, Bishop, Rook, or Queen.\n")
                                    for key,value in promoptions.items():
                                        if promochoice.title() == key:
                                            board[usermove[3:5]] = "B" + value
                                            blackmovelist.append(usermove[3:5] + "=" + value + " ")
                                            savefile = open("savereplay.txt", "a")
                                            savefile.write(usermove[0:2] + value + usermove[3:5])
                                            savefile.close()
                                            promoted = True
                                            #pawnPromo(colors[blackcolor],promochoice.title())
                        #or two spaces
                        elif int(usermove[1]) - int(usermove[4]) == 2 and int(usermove[1]) == 7:
                            if targetspace == '  ' and bpawninbetween == '  ':
                                moveable = True
                                piecemove(piece,usermove,whitemove)
                                if moveable == True:
                                    turnrecorded = True
                                    blackmovelist.append(usermove[3:5] + "     ")
                    #black pawn capture
                    if targetspace[0].lower() == "w":
                        if abs(ord(usermove[0]) - ord(usermove[3])) == int(usermove[1]) - int(usermove[4]) == 1:
                            moveable = True
                            piecemove(piece,usermove,whitemove)
                            if moveable == True:
                                if usermove[4] != "1":
                                    turnrecorded = True
                                    blackmovelist.append(usermove[0] + "x" + usermove[3:5] + "   ")
                                # Promotion
                                elif usermove[4] == "1":
                                    turnrecorded = True
                                    promochoice = input("What would you like to promote to?\nKnight, Bishop, Rook, or Queen.\n")
                                    for key,value in promoptions.items():
                                        if promochoice.title() == key:
                                            board[usermove[3:5]] = "B" + value
                                            blackmovelist.append(usermove[0] + "x" + usermove[3:5] + "=" + value + " ")
                                            savefile = open("savereplay.txt", "a")
                                            savefile.write(usermove[0:2] + value + usermove[3:5])
                                            savefile.close()
                                            promoted = True
                                            #pawnPromo(colors[blackcolor],promochoice.title())
                else:
                    moveable = False
                    print("Error: tried to move invalid piece, tried to move on own piece")
            else:
                moveable = False
                print("Error: invalid input")
        except Exception as e:
            moveable = False
            print("Error")
            print(e)
    #checking if king is alive
    #WK = 'WK' in board.values()
    #BK = 'BK' in board.values()
    wkp, bkp = kingPos(wkp,bkp)

    #running perspectives, printing movelist
    if moveable == True:
        if turnrecorded == False:
            if whitemove == True:
                whitemovelist.append(piece[1] + usermove[3:5] + "    ")
            if whitemove == False:
                blackmovelist.append(piece[1] + usermove[3:5] + "    ")
        if whitemove == True and checkmate == False:
            print("\n\nBlack to move: \n")
            blackpersp(whitecolor,blackcolor)
            whitemove = False
            turnnumber += 1
            turnappend = str(turnnumber)
            turnnumberlist.append(turnappend)
        elif whitemove == False and checkmate == False:
            print("\n\nWhite to move: \n")
            whitepersp(whitecolor,blackcolor)
            whitemove = True
        print("")
        for value in turnnumberlist:
            if value != "Turn number:":
                if len(value) == 6:
                    print("Stop. This has gone far enough. There is no reason for you to do this. Do something better with your life. Please.")
                    break
                elif len(value) == 1:
                    print(turnnumberlist[counter1], end = "       ")
                elif len(value) == 2:
                    print(turnnumberlist[counter1], end = "      ")
                elif len(value) == 3:
                    print(turnnumberlist[counter1], end = "     ")
                elif len(value) == 4:
                    print(turnnumberlist[counter1], end = "    ")
                elif len(value) == 5:
                    print(turnnumberlist[counter1], end = "   ")
            else:
                print(turnnumberlist[counter1], end = " ")
            counter1 += 1
        print("")
        counter1 = 0
        for value in whitemovelist:
            print(whitemovelist[counter1], end = " ")
            counter1 += 1
        print("")
        counter1 = 0
        for value in blackmovelist:
            print(blackmovelist[counter1], end = " ")
            counter1 += 1
        print("\n")
        counter1 = 0
        if whitemove == True and turnnumber == 1:
            if replaying == False:
                savefile = open("savenotation.txt", "a")
                savefile.write("\n" + turnnumberlist[turnnumber] + ". " + whitemovelist[turnnumber] + " " + blackmovelist[turnnumber] + "\n")
        elif whitemove == True and turnnumber >= 2:
            if replaying == False:
                savefile = open("savenotation.txt", "a")
                savefile.write(turnnumberlist[turnnumber - 1] + ". " + whitemovelist[turnnumber - 1] + " " + blackmovelist[turnnumber - 1] + "\n")
                savefile.close()
        if whitemove == False and checkmate == True:
            if replaying == False:
                savefile = open("savenotation.txt", "a")
                savefile.write(turnnumberlist[turnnumber - 1] + ". " + whitemovelist[turnnumber - 1] + "#" + "\n")
                savefile.close()
                savefile = open("savereplay.txt", "a")
                savefile.write("#B   ")
                savefile.close()
        elif whitemove == True and checkmate == True:
            if replaying == False:
                savefile = open("savenotation.txt", "a")
                savefile.write("#\n")
                savefile.close()
                savefile = open("savereplay.txt", "a")
                savefile.write("#W   ")
                savefile.close()
        if firstturn == False and whitemove == True:
            turnnumberlist.remove("Turn number:")
            whitemovelist.remove("White Moves:")
            blackmovelist.remove("Black Moves:")
            firstturn = True
    else:
        print("Please enter a valid move\n")