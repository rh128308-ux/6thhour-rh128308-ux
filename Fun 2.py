#Name: Raphael Hennings
#Class: 6th
#Idea: Packlist

import random
import time
import math


print("hello world")

print("")

def gamblegame():
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
    money = 2 ^ winnum
    print(money)
    again = input("Do you want to play again? (y/n)")
    if again == "y"or "yes":
        print("okay, next round")
        gamblegame()
    else:
        print("okay, see you next time")
        operation_after_login()

def GAMBLINGsad():
    winnum = 0
    money = 1
    print("Welcome to the Casino")
    time.sleep(1)
    print("The game is called, Gamble random integer")
    print("You start with one dollar and if you win, itr gets doubled")
    gamblegame()






def operation_after_login():
    Whatnext = input("What do you wanna do?")
    if Whatnext == "":

    elif Whatnext=="":

    elif Whatnext == "":

    elif Whatnext == "":


def password():
    global password
    password = str(input("Enter your Password"))
    password_one = str(input("Enter your Password again"))
    if password == "Feyzlvr1206":
        if password == password_one:
            print("Welcome ", user)
            print(user)
            print(password)
            time.sleep(5)
            print("loading complete")
            Action = input("Are you happy? (yes/no): ")
            if Action == "yes":
                print("amazing")
                operation_after_login()

            else:
                print("Im sorry to hear")
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
    else:
        print("have a nice day")

