#Name: Raphael Hennings
#Class: 6th
#Idea: Packlist

import random
import time
import math

print("hello world")

print("")

def gamblegame():
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
        yourmoney = 1
        yourmoney = (gamble_range_max-gamble_range_min) * yourmoney
        print(yourmoney)
    else:
        print(wining_number)
        print("You lost,:(")
        print("Your new balance is")
        yourmoney = yourmoney -
        print(yourmoney)
        again = input("Do you want to play again? (y/n)")
        if again == "y"or "yes":
            print("okay, next round")
            gamblegame()
        else:
            print("okay, see you next time")
            operation_after_login()

def GAMBLINGsad():
    winnum = 0
    print("Welcome to the Casino")
    time.sleep(1)
    print("The game is called, Gamble random integer")
    print("You start with one dollar and if you win, itr gets doubled")
    gamble_range_min = int(input("Enter your Gambling Range Min"))
    gamble_range_max = int(input("Enter your Gambling Range Max"))
    print("Pick a number between", gamble_range_min, "and", gamble_range_max)
    gamblenum = int(input("Your Gambling Number: "))
    print("loading")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("loading")
    time.sleep(1)
    print("...")
    print(gamblenum)
    print("You won, amazing")
    print("Congrats")
    money = 2 ** winnum
    print(money)
    again = input("Do you want to play again? (y/n)")
    if again == "y" or "yes":
        print("okay, next round")
        GAMBLINGsad()
    else:
        print("okay, see you next time")
        operation_after_login()






def operation_after_login():
    Whatnext = input("What do you wanna do?")
    if Whatnext == "Gambling":
        print("Gambling")
        gamblegame()

    elif Whatnext=="nothing":
        print("fine too, waiting for you to decide")
        operation_after_login()

    elif Whatnext == "shut down":
        print("shuting down")
        exit()

    elif Whatnext == "restart":
        print("restarting programm")
        login() 


def password():
    global password
    password = str(input("Enter your Password"))
    password_one = str(input("Enter your Password again"))
    if password == "Feyzlvr1206":
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
                Action = input("Are you happy? (yes/no): ")
                if Action == "yes":
                    print("amazing")
                    operation_after_login()

                else:
                    print("Im sorry to hear")
                    print("then lets try to put a smile on your face")
                    print("loading")
                    time.sleep(1)
                    print("loading complete")
                    print("traveling to...")
                    time.sleep(1)
                    print("Casino")
                    GAMBLINGsad()
        else:
            print("wrong password")
            time.sleep(15)
            login()
    else:
        print("wrong password")
        time.sleep(15)
        login()

def login():
    global wifi, login, admin, log_in_int, password_one, password_two, login_in_int
Choice_one = input("do you want to log in (yes/no): ")
if Choice_one == "yes":
    user = input("Enter your Username")
    if user == "Feyzlvr":
        password()
    elif user == ("Grabschi"):
        print("no password required")
        gamblegame()
    elif user == ("Raphael"):
        print("no password required")
        GAMBLINGsad()
    elif user == ("Hadschi"):
        print("no password required")
        operation_after_login()
    else:
        print("no such user")
        print("have a nice day")

