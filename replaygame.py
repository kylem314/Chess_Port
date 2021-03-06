# Read the replayfile
replayfile = open("savereplay.txt").read()

# Defining Variables
currentletter = ""
currentmove = ""
currentcounter = 0
repersp = "white"
turncounter = 0
lastturn = False
autoplay = False
promotions = 0

# Turn printing function
def turnprint(currentcounter, promotions):
    disp = promotions * 5
    turn = currentcounter - disp
    turn = turn / 10
    turn = math.floor(turn + 1)
    strturn = str(int(turn))
    currentcounter = currentcounter
    if currentcounter % 2 == 0 and promotions % 2 == 0:
        global turnprintx
        turnprintx = "\nNext Turn: " + strturn + " Black\n\n"
        print("\nNext Turn: " + strturn + " Black")
    elif currentcounter % 2 == 1 and promotions % 2 == 1:
        turnprintx = "\nNext Turn: " + strturn + " Black\n\n"
        print("\nNext Turn: " + strturn + " Black")
    else:
        turnprintx = "\nNext Turn: " + str(int(strturn) + 1) + " White\n"
        print("\nNext Turn: " + str(int(strturn) + 1) + " White")

Keylist = ["A", "B", "C", "D", "E", "F"]
Keycheck = ""
Keychecked = False
indexing = -1
# Checking the Key
# index = replayfile.find(Key)
Key = input("\nWhat is your game key?\n")

if len(Key) != 6:
    print("Please enter a valid game key.\n")
    mainmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset)

for letter in replayfile:
    indexing += 1
    Keylist.pop(0)
    Keylist.append(replayfile[indexing])
    for keything in Keylist:
        Keycheck = Keylist[0] + Keylist[1] + Keylist[2] + Keylist[3] + Keylist[4] + Keylist[5]
    if Keycheck == Key:
        index = indexing + 1
        Keychecked = True
        replaying = True
        break
    else:
        Keycheck = ""

if Keychecked == False:
    print("Please enter a valid game key.\n")
    mainmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset)

os.system("clear")
print("\nNext Turn: 1 White\n\n")
whitepersp(whitecolor,blackcolor)

while lastturn == False:
    currentmove = ""
    if autoplay == False:
        forward = input("Type a command.  Help for command list.\n")
        forward = forward.lower()
    else:
        forward = "n"
        time.sleep(autotimer)
    #Code for moving through replay by user input
    if forward == "e" or forward == "exit":
        break

    elif forward == "help":
        print("\nType 'n' or 'next' to continue\n'f' or 'flip' to change perspectives\n'e' or 'exit' to exit\n'a #' or 'auto #' to automatically play the rest of the game, with each move being made at the specified interval of time.\n")

    elif forward == "f" or forward == "flip":
        os.system("clear")
        print(turnprintx)
        if repersp == "white":
            repersp = "black"
            blackpersp(whitecolor,blackcolor)
        elif repersp == "black":
            repersp = "white"
            print("")
            whitepersp(whitecolor,blackcolor)

    elif forward == "n" or forward == "next" and lastturn == False:
        os.system("clear")
        turnprint(currentcounter, promotions)
        for i in range(5):
            if currentletter != "#":
                currentletter = replayfile[currentcounter + index]
                currentmove = currentmove + currentletter
                currentcounter += 1
            else:
                lastturn = True
                currentletter = replayfile[currentcounter + index]
                currentmove = currentmove + currentletter
                currentcounter += 1

        #    randomvar = int(currentmove[1])
        #    promotionvariable = currentmove[0] + str(randomvar + 1)

        if currentmove != "0-0B " and currentmove != "0-0-B" and currentmove != "0-0W " and currentmove != "0-0-W" and currentmove != "#W   " and currentmove != "#B   " and currentmove[2] != "B" and currentmove[2] != "N" and currentmove[2] != "R" and currentmove [2] != "Q":
            board[currentmove[3:5]] = board[currentmove[0:2]]
            board[currentmove[0:2]] = "  "
            randomvar = int(currentmove[1])
            promotionvariable = currentmove[0] + str(randomvar + 1)

        if currentmove[2] == "B" and currentmove[0] != "#":
            if currentcounter % 2 == 0:
                board[promotionvariable] = "WB"
            else:
                board[promotionvariable] = "BB"
            promotions += 1
        elif currentmove[2] == "R":
            if currentcounter % 2 == 0:
                board[promotionvariable] = "WR"
            else:
                board[promotionvariable] = "BR"
            promotions += 1
        elif currentmove[2] == "N":
            if currentcounter % 2 == 0:
                board[promotionvariable] = "WN"
            else:
                board[promotionvariable] = "BN"
            promotions += 1
        elif currentmove[2] == "Q":
            if currentcounter % 2 == 0:
                board[promotionvariable] = "WQ"
            else:
                board[promotionvariable] = "BQ"
            promotions += 1

        elif currentmove == "0-0W ":
            board["e1"] = '  '
            board["f1"] = 'WR'
            board["g1"] = 'WK'
            board["h1"] = '  '
            currentmove = ""
        elif currentmove == "0-0B ":
            board["e8"] = '  '
            board["f8"] = 'BR'
            board["g8"] = 'BK'
            board["h8"] = '  '
            currentmove = ""
        elif currentmove == "0-0-W":
            board["a1"] = '  '
            board["b1"] = '  '
            board["c1"] = 'WK'
            board["d1"] = 'WR'
            board["e1"] = '  '
            currentmove = ""
        elif currentmove == "0-0-B":
            board["a8"] = '  '
            board["b8"] = '  '
            board["c8"] = 'BK'
            board["d8"] = 'BR'
            board["e8"] = '  '
            currentmove = ""

        elif currentmove == "#W   ":
            print("\n\nGG, White won!")

        elif currentmove == "#B   ":
            print("\n\nGG, Black won!")

        if repersp == "white":
            print("\n")
            whitepersp(whitecolor,blackcolor)
        elif repersp == "black":
            print("\n")
            blackpersp(whitecolor,blackcolor)

    elif len(forward) >= 2 and forward[0] == "a" and forward[1] == " ":
        try:
            autotimer = int(forward[2:])
            autoplay = True
        except:
            print("Please enter a valid time value")

    elif len(forward) >= 5 and forward[0:4] == "auto" and forward[4] == " ":
        try:
            autotimer = int(forward[5:])
            autoplay = True
        except:
            print("Please enter a valid time value")

    else:
        print("Please input a valid response")

"""returntomenu = input("Press enter to return to the main menu\n")
exec(open("main.py").read())
"""