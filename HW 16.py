#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: HW16


#1. import the "random" library

import random

import time

#2. print "Hello World!"

print("hello world")

#3. Create three variables named a, b, and c, and allow the user to input an integer for each.

x = int(input("enter a number"))
y = int(input("enter a number"))
z = int(input("enter a number"))

#4. Add a and b together, then divide the sum by c. Print the result.

d = (x + y)/z

print((x + y)/z)

#5. Round the result from #3 up or down, and then determine if it is even or odd.

e = round(d)
print(e)

if e % 2 == 0:
    print("even")
else:
    print("odd")

#6. Create a list of five different random integers between 1 and 10.

rand_int_LIST = [random.randint(1,10) for i in range(5)]
print(rand_int_LIST)

#7. Print the 4th number in the list.

print(rand_int_LIST[3])

#8. Append another integer to the end of the list, also random from 1 to 10.
f = random.randint(1,10)
rand_int_LIST.append(f)

#9. Sort the list from lowest to highest and then print the 4th number in the list again.

rand_int_LIST.sort()
print(rand_int_LIST[3])
time.sleep(5)

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.

i = 1
while i <= 100:
    print(i)
    i += i
    time.sleep(1)

#11. Create a list containing the names of five other students in the classroom.

names = ["Malachi","Braylee","Benson","Owen","Nate",]

#12. Create a for loop that individually prints out the names of each student in the list.

for name in names:
    print(name)
    time.sleep(1)


#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.

for a in range(1,100):
    if a%10==0:
        break
    print(a)
    time.sleep(1)


#14. Free space. Do something creative. :)

