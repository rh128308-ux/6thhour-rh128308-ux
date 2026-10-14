#Name:Raphael Hennings
#Class: 6th Hour
#Assignment: HW12
import time
import random

#1. Print Hello World!

print("Hello World!")

#2. Create three different boolean variables named wifi, login, and admin.

wifi =  True
login = True
admin = True

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.

log_in_int = 0

#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

def gf():
    gfq = input("Is your family sick? (yes/no):")
    if gfq == "yes":
        print(" that is great")


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



def login():
    global wifi, login, admin, log_in_int, password_one, password_two, login_in_int
Choice_one = input("do you want to log in (yes/no): ")
if Choice_one == "yes":
    login_in_int = 0
    user = input("Enter your Username")
    password = str(input("Enter your Password"))
    password_one = str(input("Enter your Password again"))
    if password == "AOT":
        if password == password_one:
            print("Welcome ",user)
            print(user)
            print(password)
            time.sleep(5)
            print("loading complete")
            Action = input("Are you happy? (yes/no): ")
            if Action == "yes":
                print("amazing")

            else:
                joke()
        elif log_in_int >= 3:
            print("login incorrect")
            print("3 failed tries")
            time.sleep(25)
            print("try again")
            login()
    elif log_in_int >= 3:
        login_in_int += 1
        print("login incorrect")
        print("3 failed tries")
        time.sleep(25)
        print("try again")
        login()
else:
    print("have a nice day")


def logingamble():
    global wifi, login, admin, log_in_int, password_one, password_two, login_in_int
Choice_one = input("do you want to log in (yes/no): ")
if Choice_one == "yes":
    login_in_int = 0
    user = input("Enter your Username")
    password = str(input("Enter your Password"))
    password_one = str(input("Enter your Password again"))
    if password == "AOT":
        if password == password_one:
            gambling = random.randint(1,100)
            if gambling == 1:
                print("Welcome ",user)
                log_in_int += 1
            else:
                print("Wrong Password. Try Again")
                print("3 failed tries")
                time.sleep(25)
                print("try again")
                login()
    elif log_in_int >= 3:
        print("login incorrect")
        print("3 failed tries")
        time.sleep(25)
        print("try again")
        login()

else:
    exit()

if wifi == True:
    if login == True:
        if admin == True:
            login()

        else:
            print("access denied")
    else:
        print("access denied")
else:
    print("access denied")

