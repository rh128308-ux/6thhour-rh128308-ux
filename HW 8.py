#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library

import random

#2. print "Hello World!"

print("Hello World!")

#3. Create three different variables that each randomly generate an integer between 1 and 10

randint1 = random.randint(1,10)
randint2 = random.randint(1,10)
randint3 = random.randint(1,10)

#4. Print the three variables from #3 on the same line.

print(randint1, randint2, randint3)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
radintsum = randint1 + 2
randintsub = randint2 - 4
randintprod = randint3 * 1.5

#6. Print each result from #5 on the same line.

print(radintsum, randintsub, randintprod)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6


fourrandintlist =  [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]

#8. Sort the list in #7 and print it.

fourrandintlist.sort()
print(fourrandintlist)

#9. Add together the highest three numbers in the list from #7 and print the result.

fourrandintlist.sort(reverse=True)
sumofthreehighest = fourrandintlist[0] + fourrandintlist[1] + fourrandintlist[2]
print(sumofthreehighest)
fourrandintlist.sort()

#10. Create a list with 5 names of other students in this class and print the list.

studentsnamelist = ["Braylee", "Malachi", "Bensen", "Owyn, Raphael"]
print(studentsnamelist)

#11. Shuffle the list in #10 and print the list again.

random.shuffle(studentsnamelist)
print(studentsnamelist)

#12. Print a random choice from the list of names from #10.

print(random.choice(studentsnamelist))
