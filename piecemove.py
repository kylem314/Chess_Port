#exec(open("check.py").read())
exec(open("kingmove.py").read())
# Piecemove Function
#print(wkingmove(usermove,board,whiteking))
revertstart = board[usermove[0:2]]
revertend = board[usermove[3:5]]
board[usermove[0:2]] = '  '
board[usermove[3:5]] = piece
#global moveable
#if whitemove == True and whitecheck(usermove,board,whiteking) == True or whitemove == False and blackcheck(usermove,board,blackking) == True:
#  moveable = False
#  board[usermove[0:2]] = revertstart
#  board[usermove[3:5]] = revertend
#else:
global turnrecorded
if revertend != "  " and piece[1] != 'p':
    if whitemove == True:
        whitemovelist.append(piece[1] + "x" + usermove[3:5] + "   ")
    else:
        blackmovelist.append(piece[1] + "x" + usermove[3:5] + "   ")
    turnrecorded = True
if replaying == False and usermove != "0-0" and usermove != "0-0  " and usermove != "0-0-0":
    savefile = open("savereplay.txt", "a")
    savefile.write(usermove)
    savefile.close()