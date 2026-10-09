#Name:Raphael Hennings
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"

print("Hello World!")

#2. Create a list with three variables that each randomly generate a number between 1 and 100

rand_num_list = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]

#3. Print the list.

print(rand_num_list)

#4. Create an if statement that determines which of the three numbers is the highest and prints the result.

if rand_num_list[0] > rand_num_list[1] and rand_num_list[0] > rand_num_list[2] :
    print(rand_num_list[0],"is the highest number(1st integer in the list)")
elif rand_num_list[1] > rand_num_list[0] and rand_num_list[1] > rand_num_list[2] :
    print(rand_num_list[1],"is the highest number(2nd integer in the list)")
else:
    print(rand_num_list[2],"is the highest number(3rd integer in the list)")


#5. Tie the result (the largest number) from #4 to a variable called "num".

num = max(rand_num_list[0], rand_num_list[1], rand_num_list[2])

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num%2 == 0:
    if num%3 == 0:
        print("num is divisible by 2 and 3")
    else:
        print("num is divisible by 2, but not 3")

elif num%3 == 0:
    print("num is divisible by 3, but not 2")

else:
    print("num is divisible neither by 3 or 2  ")


