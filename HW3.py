#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: HW3
import math

#1. Print "Hello World!"

print("Hello world")

#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.

intVar27 = 96

strVar28 = "Hello Dr. Tenma"

boolVar29 = False

#3. Print all three variables on the same print function (at the same time).

print(intVar27,strVar28,boolVar29)

#4. Create a variable that asks the user to input an integer.

intuser = int(input("Enter a number, please:"))
print(intuser)

#5. Add the integer variable from #2 with the integer from #4 and print the result.

comb_int = (intuser+intVar27)

print(comb_int)

#6. Take the result from #5 and divide it by 2. Print the result.

div_int = (comb_int/2)

print(div_int)

#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).

boolVar29 = True

#8. Print the value of the boolean variable.

print(boolVar29)

#9. Create a variable with a number that contains decimals.

var30 = 3.1415

#10. Round the number from #9 up or down using the round function.

print(round(var30))
