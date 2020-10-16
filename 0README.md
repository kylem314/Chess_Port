# Welcome to our ASCII Chess Game!

Our program's main purpose is to enable you to play chess with other players.  However, you can also change the colors of your pieces through settings, save and replay games, and play other chess-based gamemodes (WIP)

## How to use

After running the code, a main menu should appear.  Simply follow the page headings to navigate through the program.  If you don't know how to play chess, Rules is a good place to start.

## File Descriptions

#### Note - Some files may start with "z's", just to organize in file list

### General files

main.py - Many functions defined here, runs the starting menu which links to other files
0README.md - Starting file detailing our program

### Code files


movepiece.py - Functions to check if a piece is able to move to a position, as well as taking in userinputs and printing the boards defined here
piecemove.py - Short funtion to move and record the piece movements
replaygame.py - Replaying games from a savefile
zblackpersp.py - Printing black perspective view
zwhitepersp.py - Printing white perspective view
check.py (Not running. Incomplete)- How the program defines checks is defined here
kingmove.py (Not running. In progress)

### Save files

savenotation.txt - A file users can read in order to look at their previous games in actual chess notation (ctrl+f to find using game key)
savereplay.txt - Program file not meant to be read by users - saves data in a more condensed form to be read by the program when replaying past games.
#### May encrypt this file for fun - Kyle

### Other text files

zzdump.txt - Pieces of our code we may need later (ex. testing things, old portions that may have been replaced, saving strings/data)
zzzrules.txt - File the program reads when someone enters "3. Rules" in settings.  This is just to make the code itself less cluttered with a long string.

## Creators

DNHS AP CS Principles, Taught by Mr. Mortenson 
Group Colin A - 

Kyle Myint
David Kim
Colin Szeto
Devam Shrivastava
Shekar Krishnamoorthy

## AP Requirements

#### Note: There are many uses of all of these concepts - listed below are just a few examples of each
```
Variables and Assignments    -      Main.py         -     lines 69-101
Mathematical Expressions     -      Check.py        -     lines 7-25
Boolean Expressions          -      Movepiece.py    -     lines 418-443
Conditionals                 -     Kingmove.py      -     lines 15-30
Nested Conditionals          -     Movepiece.py     -     Essentially all of it
Iteration                    -     Check.py         -     lines 55, 68, 87
Developing Algorithms        -     Main.py          -     lines 8-50
Lists                        -     Zblackpersp.py   -     lines 1-36
Libraries                    -     Main.py          -     lines 2, 21
Random Values                -     Main.py          -     lines 20-24
```

## Versions   

Latest: This file

9/17/20 - https://repl.it/@KyleMyint/ASCII-Chess-3
Changes: 

9/16/20 - https://repl.it/@KyleMyint/ASCII-Chess-1
Changes:

9/12/20 - https://repl.it/@KyleMyint/ASCII-Chess-1-91220
Changes:

9/11/20 - https://repl.it/@KyleMyint/ASCII-Chess-Backup
Changes:

## TODO

* Be able to change color in settings for blackpersp
* Complete check function and integrate into code
* Checkmate/stalemate
* New gamemodes in 1. start game
* Special pawn moves
* Fix bug when things print move twice when capturing