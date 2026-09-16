#Name:Raphael Hennings
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

mediannum = intlist.pop(4)
emplist.append(mediannum)

#5. Remove the first number from the first list and add it to the second list.

mediannumtwo = intlist.pop(0)
emplist.append(mediannumtwo)

#6. Print both lists.

print(emplist)
print(intlist)

#7. Add the two numbers in the second list together and print the result.

emplistsum = (emplist[0] + emplist[1])
print(emplistsum)

#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

intlist.append(emplistsum)

#9. Sort the first list from lowest to highest and print it.

intlist.sort(reverse=False)
print(intlist)