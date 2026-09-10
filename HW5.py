#Name:Raphael Hennings
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!

print("Hello World")

#1. Create a list with 5 strings containing 5 different names in it.

strlist = ["Rhett","Kinsley","Malachi","Landon","JJ",]

#2. Append a new name onto the Name List.

strlist.append("Jakob")

#3. Print out the 4th name on the list.

print(strlist[3])

#4. Create a list with 4 different integers in it.

intlist = [703,2407,1206,48,40]

#5. Insert a new integer into the 2nd spot and print the new list.

intlist.insert(1, 43731)

#6. Sort the list from lowest to highest and print the sorted list.

intlist.sort (reverse=False)

#7. Add the 1st three numbers on the sorted list together and print the sum.

addintlist = intlist[0] + intlist[1] + intlist[2]

print(addintlist)

#8. Create a list with two strings, two variables, and two boolean values.

twotwotwolist = ["Hiro", 16, False, "ZeroTwo", 2, False ]
#I'm not a fan of darling in the franxx im just watching it

#9. Create a print statement that asks the user to input their own index value for the list on #8.

print(twotwotwolist[int(input("enter index location:"))-1])