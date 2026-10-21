#Name:Raphael Hennings
#Class: 6th Hour
#Assignment: HW13

import random

print("Hello World!")

#1. Import the random function

#look line 5

#2. Create a variable called 'temp' that randomly generates a number between 1 and 30
temp = random.randint(1,30)
#3. Go to the link below and convert the flowchart into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

# If temp higher 20
#       print it's hot
# Elif temp higher than 10
#       print it's mild
# Else
#       print It's cold
# print Thank you!

if temp > 20:
    print("It's hot")
elif temp > 10:
    print("It's mild")
else:
    print("It's cold")
print("Thank you!")