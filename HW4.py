#Name:Raphael Hennings
#Class: 6th Hour
#Assignment: HW4
import math

#1. Print "Hello World!"

print("Hello World")

#2. import the 'math' library


#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.

floatx= float(input("enter a decimal number"))

inty= int(input("enter a whole number/integer"))

#4. Create a variable with the value that is x and y added together.

floataddVofxy = floatx + inty

#5. Print the variable from #4.

print(floataddVofxy)

#6. Create a variable with the value that is x and y added together, then divide the sum by 3.

Vofxydb3 = floataddVofxy/3

#7. Print the variable from #6.

print(Vofxydb3)

#8. Create a variable with the value of the squaregg root of y, then print the result.

sry = math.sqrt(inty)
print(sry)

#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.

rofloatx = round(floatx, 1)
print(rofloatx)

#10. Use the ceiling function to round x up to the nearest whole number. Print the result.

rtcofx = round(math.ceil(floatx))
print(rtcofx)

#11. Use the floor function to round x down to the nearest whole number. Print the result.

rtfofx = round(math.ceil(floatx))
print(rtfofx)