# imports
import uuid
import math
import time
import os
from random import randrange
from animation import *

#import username/password function
exec(open("password.py").read())

# Function Definitions
exec(open("check.py").read())
exec(open("kingmove.py").read())


#classes to call
def whitepersp(whitecolor,blackcolor):
    exec(open("zwhitepersp.py").read())
def blackpersp(whitecolor,blackcolor):
    exec(open("zblackpersp.py").read())
def movepiece():
    exec(open("movepiece.py").read())
def main():
    exec(open("main.py").read())
def check():
    exec(open("check.py").read())
def replaygame():
    exec(open("replaygame.py").read())
def key(string_length=10):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]
def settingmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset):
    while settingexit == False:
        try:
            print(colors[whitecolor] + "\nWhite Piece Color - " + whitecolor + colors[blackcolor] + "\nBlack Piece Color - " + blackcolor + u"\u001b[0m")
        except:
            print("Please enter a valid color")
        for key,value in colors.items():
            if key != "electric blue":
                print(value + key, end = ", ")
            else:
                print(value + key + u"\u001b[0m")
        print("\nType white,color or black,color to change the piece colors (ex. white,orange)")
        print("Type exit to return to the menu\n")
        setting = input("What would you like to do? \n")
        setting = setting.lower()
        if setting[:6] == "white,":
            whitecolor = setting[6:]
        elif setting[:6] == "black,":
            blackcolor = setting[6:]
        elif setting == "exit":
            settingexit = True
            print("")
        else:
            print("Please enter a valid response\n")
    global colorsets
    colorsets = whitecolor + "!" + blackcolor


# Board Dictionary
board = {
    "a8":"BR", "b8":"BN", "c8":"BB", "d8":"BQ", "e8":"BK", "f8":"BB", "g8":"BN", "h8":"BR",
    "a7":"bp", "b7":"bp", "c7":"bp", "d7":"bp", "e7":"bp", "f7":"bp", "g7":"bp", "h7":"bp",
    "a6":"  ", "b6":"  ", "c6":"  ", "d6":"  ", "e6":"  ", "f6":"  ", "g6":"  ", "h6":"  ",
    "a5":"  ", "b5":"  ", "c5":"  ", "d5":"  ", "e5":"  ", "f5":"  ", "g5":"  ", "h5":"  ",
    "a4":"  ", "b4":"  ", "c4":"  ", "d4":"  ", "e4":"  ", "f4":"  ", "g4":"  ", "h4":"  ",
    "a3":"  ", "b3":"  ", "c3":"  ", "d3":"  ", "e3":"  ", "f3":"  ", "g3":"  ", "h3":"  ",
    "a2":"wp", "b2":"wp", "c2":"wp", "d2":"wp", "e2":"wp", "f2":"wp", "g2":"wp", "h2":"wp",
    "a1":"WR", "b1":"WN", "c1":"WB", "d1":"WQ", "e1":"WK", "f1":"WB", "g1":"WN", "h1":"WR"}

# Colors Dictionary
colors = {"pink":u"\u001B[31m", "neon green":u"\u001B[32m","orange":u"\u001B[33m", "blue":u"\u001B[34m", "purple":u"\u001B[35m", "lighter blue":u"\u001B[36m", "red":u"\u001B[91m", "green":u"\u001B[92m", "orange yellow":u"\u001B[93m", "lavender":u"\u001B[95m", "electric blue":u"\u001B[96m"}

# Variable Definitions

Key = key(6)
text = ["BR", "BN", "BB", "BQ", "BK", "bp", "WR", "WN", "WB", "WQ", "WK", "wp"]
piece = ["♜ ","♞ ","♝ ","♛ ","♚ ","♟ ","♜ ","♞ ","♝ ","♛ ","♚ ","♟ "]
promoptions = {"Knight":"N", "Bishop":"B", "Rook":"R", "Queen":"Q"}
turnnumber = 0
turnappend = ""
turnnumberlist = ["Turn number:"]
whitemovelist = ["White Moves:"]
blackmovelist = ["Black Moves:"]
testvar1 = "hi"
testvar2 = "bye"
testvar3 = -1
counter1 = 0
whitemove = True
checkmate = False
wkcastle = True
wqcastle = True
bkcastle = True
bqcastle = True
firstturn = False
squarecheck = 0
whitecolor = "red"
blackcolor = "lighter blue"
replaying = False
whiteking = "e1"
blackking = "e8"
exited = False
colorset = ""
settingexit = False
capturing = False
moveable = False
turnrecorded = False
wkspaces = []
bkspaces = []
wkp = ""
bkp = ""
#black color: 36 or 95
# Key duplicate check
def mainmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset):

    os.system("clear")

    replayfile = open("savereplay.txt").read()
    indexx = replayfile.find(Key)
    while indexx != -1:
        if indexx == -1:
            pass
        else:
            Key = key(6)

    # Welcome message
    print("Welcome to ASCII Chess! \n")
    print("================\nMenu:\n1. Start Game\n2. Play Replay\n3. Rules\n4. Settings\n5. Exit\n================\n")
    start = input("What would you like to do?\n")
    start = start.lower()


    # Start Menu

    if start == "1" or start == "start game":
        print("")
        savefile = open("savereplay.txt", "a")
        savefile.write(Key)
        savefile.close()
        savefile = open("savenotation.txt", "a")
        savefile.write(Key)
        savefile.close()
        whitepersp(whitecolor,blackcolor)
        movepiece()

    elif start == "2" or start == "play replay":
        replaygame()

    elif start == "3" or start == "rules":
        file = open("zzzrules.txt").read()
        print("\n" + file + "\n")
        exit = input("Type exit to return to the menu\n")
        exit = exit.lower()
        while exited == False:
            if exit == "exit":
                print("")
                mainmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset)
            else:
                print("Please enter a valid response\n")
            exit = input("Type exit to return to the menu\n")
            exit = exit.lower()

    elif start == "4" or start == "settings":
        indexerthing = 0
        settingmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset)
        for letter in colorsets:
            indexerthing += 1
            if letter == "!":
                break
        whitecolor = colorsets[:indexerthing - 1]
        blackcolor = colorsets[indexerthing:]
        mainmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset)

    elif start == "5" or start == "exit":
        print("\nwow rude")

    else:
        print("Please type a valid choice. \n")
        mainmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset)
menuAni() #loading animation when you want to
mainmenu(Key,key,replaying,exited,settingexit,whitecolor,blackcolor,colorset)

