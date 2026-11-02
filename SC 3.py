#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: SC3
import time

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.

x = 0

while x <=100:
    x += 1
    if x % 3 == 0:
        if x % 5 == 0:
            time.sleep(1)
            print("FizzBuzz")

        else:
            time.sleep(1)
            print("Fizz")

    elif x % 5 == 0:
        time.sleep(1)
        print("Buzz")

    else:
        print(x)
        time.sleep(1)
        continue


