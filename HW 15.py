#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: HW15

import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

for i in range(5, 0, -1):
    print(i)
print("hello world")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.

for i in range(1,31):
    if i % 2 == 0:
        print(i)

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.

for i in range(1,31):
    if i % 3 == 0:
        continue
    else:
        print(i)

#4. Create a for loop that prints 5 different animals from a list.

for animal in ["dog", "cat", "bird", "mouse","fly"]:
    print(animal)

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

word = input("Enter a word")
txt = word[::-1]
print(txt)

#6. Create a list containing 10 integers of your choice and print the list.
want_int_list = [1,2,3,4,5,6,7,8,9,1206]

#7. Create two empty variables named evenNumbers and oddNumbers.

evenNumbers = []
oddNumbers = []

#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.

e = 0
o = 0

for l in want_int_list:
    if l % 2 == 0:
        e+= 1
    else:
        o += 1

print(e)
print(o)

#9. Create a variable that asks the user for an integer and an empty integer variable.

f = int(input("Enter a number"))
empint = 0

#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)

j = 1

for i in range(1,f +1):
    j *= i
    print(j)
    time.sleep(2)
















