OOGABOOGA=1
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
import time
import os

"""
Kyle's password is kyleiscool
Shekar's password is thegoat
David's password is penspinner
Colin's password is iamcolin
Devam's password is mrscrummaster
GUEST's password is GUEST
"""

"""
        savefile = open("file.txt", "a")
        savefile.write("thing")
        savefile.close()
"""

def password_code():
    username_credentials=["Kyle", "Shekar", "GUEST", "Devam"]
    def username_give():
        print("\nFirst authorized user is player 1 (white)"+"\nSecond authorized user is player 2 (black)"+"\nPlease enter username: "+"\nType GUEST to use guest account")
    def password_give():
        print("Please enter password: "+"\nType GUEST to use guest account")
    z=1
    y=True
    x=False
    w=False
    username_give()
    username_input=input("")
    while(username_input not in username_credentials):
        if(z==1):
            print(bcolors.FAIL+bcolors.BOLD+"invalid"+bcolors.ENDC)
            username_give()
            username_input=input("")
            if(username_input in username_credentials):
                password_give()
                password_input=input("")
                if(password_input=="kyleiscool")and(username_input=="Kyle"):
                    x=True
                if(password_input=="thegoat")and(username_input=="Shekar"):
                    x=True
                if(password_input=="GUEST")and(username_input=="GUEST"):
                    x=True
                if(password_input=="mrscrummaster")and(username_input=="Devam"):
                    x=True
                y=False
                while(x==False):
                    print(bcolors.FAIL+bcolors.BOLD+"invalid"+bcolors.ENDC)
                    password_give()
                    password_input=input("")
                    y=False
                    if(password_input=="kyleiscool")and(username_input=="Kyle"):
                        x=True
                    if(password_input=="thegoat")and(username_input=="Shekar"):
                        x=True
                    if(password_input=="GUEST")and(username_input=="GUEST"):
                        x=True
                    if(password_input=="mrscrummaster")and(username_input=="Devam"):
                        x=True
    if(y==True):
        password_give()
        password_input=input("")
        x=False
        if(password_input=="kyleiscool")and(username_input=="Kyle"):
            x=True
        if(password_input=="thegoat")and(username_input=="Shekar"):
            x=True
        if(password_input=="GUEST")and(username_input=="GUEST"):
            x=True
        if(password_input=="mrscrummaster")and(username_input=="Devam"):
            x=True
        while(x==False):
            print(bcolors.FAIL+bcolors.BOLD+"invalid"+bcolors.ENDC)
            password_give()
            password_input=input("")
            if(password_input=="kyleiscool")and(username_input=="Kyle"):
                x=True
            if(password_input=="thegoat")and(username_input=="Shekar"):
                x=True
            if(password_input=="GUEST")and(username_input=="GUEST"):
                x=True
            if(password_input=="mrscrummaster")and(username_input=="Devam"):
                x=True

    print(bcolors.OKGREEN+bcolors.BOLD+"PLAYER "+str(OOGABOOGA)+" SUCCESSFULLY LOGGED IN"+bcolors.ENDC)
    if(password_input=="GUEST"):
        print(bcolors.OKGREEN+"You are using temporary guest account"+bcolors.ENDC)

        w=True
    if(w==False):
        print(bcolors.OKGREEN+"Hello "+username_input+bcolors.ENDC)

account_state=True
def neworexisting():
    print("login with existing account or new account"+"\nenter New for new account and Existing for existing account")
    first_input=input("")
    if(first_input.title() == "New"):
        account_state = False
    elif(first_input.title() == "Existing"):
        account_state = True
    else:
        neworexisting()
    return(account_state)
#account_state = neworexisting()

"""if(account_state==True):
  password_code()
  OOGABOOGA=2
  password_code()
  print(bcolors.OKBLUE+bcolors.BOLD+"\nBOTH PLAYERS HAVE SUCCESSFULLY LOGGED IN"+bcolors.ENDC)
  time.sleep(2.5)
  os.system("clear")
if(account_state==False):
  print("hi")
  time.sleep(5)"""
# need to make it ask for a new or existing account for p2