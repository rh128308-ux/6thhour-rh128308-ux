#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: SC4

import time

import math

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

import random as r

print("hello world")

modeldict = []

playerrange = int(input("enter the number of players: "))

for i in range(playerrange):
    rating  = int(input("enter your rating (between 1-5 Stars) player"+ str(i+1)))
    if rating > 5:
        print("rating too high")
        rating = 5

    elif rating < 1:
        print("rating too low")
        rating = 1
    else:
        modeldict.append(rating)

average = sum(modeldict) / playerrange
print(average)








