#Name:Raphael Hennings
#Class: 6th Hour
#Assignment: Playground

#ITS NOIT FINISSHHHHEDDDD ::::::((((((

#imports
import random
import time

from fun3 import gambling

def gamblingalone():
    winnum = 0
    gamble_range_min = int(input("Enter your Gambling Range Min"))
    gamble_range_max = int(input("Enter your Gambling Range Max"))
    print("Pick a number between", gamble_range_min, "and", gamble_range_max)
    gamblenum = int(input("Your Gambling Number: "))
    wining_number = random.randint(gamble_range_min, gamblenum)
    print("loading")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("loading")
    time.sleep(1)
    print("...")
    if wining_number == gamblenum:
        print(gamblenum)
        print("You won, amazing")
        print("Congrats")
        yourmoney = 3
        yourmoney = (gamble_range_max-gamble_range_min) * yourmoney
        print(yourmoney)
    else:
        print(wining_number)
        print("You lost,:(")
        print("Your new balance is")
        yourmoney = 0
        print(yourmoney)
        again = input("Do you want to play again? (y/n)")
        if again == "y" or "yes":
            print("okay, next round")
            gamblingalone()
        else:
            print("okay, see you next time")
            restart = input("Would you like to restart? (y/n)")
            if restart == "y" or "yes":
                login()

def gamblingtogether():
    playernum = int(input("Enter your Player Number: "))
    for x in range(playernum):
        play = {
        "1" : {
            "name" : "Orc_1",
            "money" : 1000,
            "guess" : 6
            },
        "2" : {
            "name" : "Orc_1",
            "money" : 1000,
            "guess" : 6
            },
        "3" : {
            "name" : "Orc_1",
            "health" : 1206,
            "guess" : 6
            }

        }



    gamble_range_min = int(input("Enter your Gambling Range Min"))
    gamble_range_max = int(input("Enter your Gambling Range Max"))
    print("Pick a number between", gamble_range_min, "and", gamble_range_max)
    gamblenum = int(input("Your Gambling Number: "))
    wining_number = random.randint(gamble_range_min, gamblenum)
    print("loading")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("loading")
    time.sleep(1)
    print("...")
    if wining_number == gamblenum:
        print(gamblenum)
        print("You won, amazing")
        print("Congrats")
        yourmoney = 3
        yourmoney = (gamble_range_max - gamble_range_min) * yourmoney
        print(yourmoney)
    else:
        print(wining_number)
        print("You lost,:(")
        print("Your new balance is")
        yourmoney = 0
        print(yourmoney)
        again = input("Do you want to play again? (y/n)")
        if again == "y" or "yes":
            print("okay, next round")
            gamblingalone()
        else:
            print("okay, see you next time")
            restart = input("Would you like to restart? (y/n)")
            if restart == "y" or "yes":
                login()


def settings():
    global joke



def joke():
    joke = input("Do you want to joke (yes/no): ")
    if joke == "yes":
        print("Warum sind Seerauber schlecht im kreise berechnen?")
        answer = input("do you know? (yes/no):")
        if answer == "no":
            print("weil sie PI-raten")
        elif answer == "yes":
            print("Oh, then do you wanna hear another joke?")
            joke2 = input("")
            if joke2 == "yes":
                print("Was macht ein Clown im Buro?")
                answer2 = input("do you know? (yes/no):")
                if answer2 == "no":
                    print("Faxxen")
                elif answer2 == "yes":
                    print("You really know what you are doing")
                    print("Im out of jokes, guess you have to do something else")
                    afterlogin()
    elif joke == "no":
        print("Guess not")

def afterlogin():
    print("1. Do you wanna hear a joke?")
    print("2. Do you wanna gamble?")
    print("3. or do you wanna change your settings?")
    do = input("What shall it be (1,2 or 3):")
    if do == "1":
        two = input("are you playing alone or with more people")
        if two == "alone":
            gamblingalone()

        else:
            gamblingtogether()

    elif do == "2":
        joke()
    elif do == "3":
        settings()



def password():
    global password
    passowrd = "not my birthday"
    password = str(input("Enter your Password"))
    password_one = str(input("Enter your Password again"))
    if password == passowrd:
        if password == password_one:
            print("checking user")
            print("...")
            time.sleep(1)
            print("user accepted")
            time.sleep(1)
            print("checking password")
            print("...")
            time.sleep(1)
            print("password accepted")
            time.sleep(1)
            wifiint = random.randint(1, 10)
            if wifiint == 1:
                print("checking wifi")
                print("...")
                time.sleep(1)
                print("wifi not accepted")
                exit()
            else:

                print("checking wifi")
                print("...")
                time.sleep(1)
                print("wifi accepted")
                print("Welcome ", user)
                print(user)
                print(password)
                print("loading")
                print("...")
                time.sleep(1)
                time.sleep(5)
                print("loading complete")
                print("Welcome ")
                afterlogin()

        else:
            print("wrong password")
            time.sleep(15)
            login()
    else:
        print("wrong password")
        time.sleep(15)
        login()


def login():
    global user
    Choice_one = input("do you want to log in (yes/no): ")
    if Choice_one == "yes":
        user = input("Enter your Username")
        if user == "aotlvr":
            password()

        elif user == "gmblvrs":
            gamblingalone()

