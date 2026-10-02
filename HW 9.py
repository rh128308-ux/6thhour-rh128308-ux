#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: HW9
import random

#1. Print Hello World!

print("Hello World!")

#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.

three_key_dictonary = {

    "name" : "Benson",
    "age" : 17,
    "height" : [6, 5.11, 6.1],
}

#3. Print the keys of the dictionary from #2.

print(three_key_dictonary.keys())

#4. Print the values of the dictionary from #2

print(three_key_dictonary.values())

#5. Print one of the three numbers from the list by itself

#couldn't choose...
randint = random.randint(0, 2)
print(three_key_dictonary["height"][randint])

#6. Using the update function, add a fourth key to the dictionary and give it a value.

three_key_dictonary.update({"weight" : 152})

#7. Print the entire dictionary from #2 with the updated key and value.

print(three_key_dictonary)

#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.

studentdictionary = {
        "Student1" : {
                "name" : "Benson",
                "age" : 17,
                "height" : 6
        },

        "Student2": {
                "name" : "Braylee",
                "age" : 17,
                "height" : 5.11,

        },
        "Student3" : {
                "name" : "Malachi",
                "age" : 17,
                "height" : 5.6
        }
}

#9. Print the names of all three classmates on the same line.

print(studentdictionary["Student1"]["name"],studentdictionary["Student2"]["name"],studentdictionary["Student3"]["name"])

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.

studentdictionary.pop("Student1")
print(studentdictionary)
