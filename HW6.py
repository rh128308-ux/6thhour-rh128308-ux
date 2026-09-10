#Name:Raphael Hennings
#Class: 5th Hour
#Assignment: HW6
from statistics import median

#print
print("Hello World")

#1. Create a list with 9 different numbers inside.

intlist = [ 1,2,3,4,5,6,7,8,9]

#2. Sort the list from highest to lowest.

intlist.sort(reverse=True)
#3. Create an empty list.

emplist = []

#4. Remove the median number from the first list and add it to the second list.

intmintlist = median(intlist)
emplist.insert(0,intmintlist)


#5. Remove the first number from the first list and add it to the second list.

intzeroofintlist = intlist[0]
emplist.insert(0,intzeroofintlist)
del intlist[0]

#6. Print both lists.

print(emplist)
print(intlist)

#7. Add the two numbers in the second list together and print the result.

print(emplist[0] + emplist[1])

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

intlist.sort(reverse=False)
intnineofemplist = emplist[0]
intmedianofemplist = emplist[1]
intlist.insert(0,intnineofemplist)
intlist.insert(0,intmedianofemplist)

#9. Sort the first list from lowest to highest and print it.

intlist.sort(reverse=False)
print(intlist)