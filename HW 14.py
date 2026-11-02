# Name: Raphael Hennings
# Class: 6th Hour
# Assignment: HW14

import random

# 1. Create a while loop with variable i that counts down from 5 to 0 and then prints
# "Hello World!" at the end.

print("this is number one")

i = 5

while i >= 0:
    print(i)
    i -= 1

# 2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).

print(" this is number two")
j = 0

while j <= 30:
    j += 1
    if j % 2 == 0:
        print(j)
        print("is even")
    else:
        continue


# 3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
# number is divisible by 3.

print("this is number three")

k = 0

while k < 30:
    k += 1
    if k % 3 == 0:
       continue
    else:
        print(k)
        print("is not divisible by three")




# 4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
# and then breaks the loop if it's a 1.

l = random.randint(1, 6)

while l != 1:
    print(l)
    l = random.randint(1, 6)
    if l == 1:
        print("l = 1")
        break
    else:
        continue

# 5. Create a while loop that asks for a number input until the user inputs the number 0.

m = input("input another number")

while m >= "0":
    if m == "0":
        print("this is the right number")
        break
    else:
        m = input("input another number")


