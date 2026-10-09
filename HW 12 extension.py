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




def login():
    global wifi
    global login
    global admin
    global log_in
    global password_one
    global password_two
    global login_in_intn
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






