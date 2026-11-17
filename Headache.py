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

player_list = {}


player_count = int(input("How many models?"))

for i in range(player_count):
    player_list["model_" + str(i + 1)] = {}
    player_list["model_" + str(i + 1)].update({"Name": "model " + str(i + 1),
                                                "rating": []
                                                })



print(player_list)
def rate():
    for i in range(player_count):
        print("player" + str(i + 1),"'s rating turn")
        for j in range(player_count-1):
            u = int(input("Rating of model " + str(j + 1) + ": "))
            if u < 1:
                print("rating too low")
                u = 1
                player_list["model_" + str(j + 1)].update({"rating": 0})

            elif u > 5:
                print("rating too high")
                u = 5
                player_list["model_" + str(j + 1)].update({"rating": u})
            else:
                print("rating ok")
                player_list["model_" + str(j + 1)].

rate()


x = 0


average_score = x/player_count
print("average: ",average_score)