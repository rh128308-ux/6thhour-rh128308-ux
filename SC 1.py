#Name: Raphael Hennings
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's dams well as haviage values for balancing, ang it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemy_creature_dictionary = {
     "E1" : {
        "name" : "Orc_1",
        "health" : 1206,
        "damage" : 6,
        "armor"  : 28
        },
     "E2" : {
        "name" : "Orc_2",
        "health" : 1206,
        "damage" : 6,
        "armor"  : 28
        },
     "E3" : {
        "name" : "Orc_3",
        "health" : 1206,
        "damage" : 6,
        "armor"  : 28
        },
     "E4" : {
        "name" : "Orc_4",
        "health" : 1206,
        "damage" : 6,
        "armor"  : 28
        },
     "E5" : {
        "name" : "Orc_5",
        "health" : 1206,
        "damage" : 6,
        "armor"  : 28
        },
}


def stat_change():

   Enemynumber_str = str(input("Which Enemies attackdamge do you wanna change?(E1,E2,E3,E4,E5)"))
   Enemy_key_str = str(input("What stat do you wanna change?(health,damage,armor)"))
   Change_of_stat = int(input("How high should be the stat?"))
   enemy_creature_dictionary[Enemynumber_str].update({Enemy_key_str: Change_of_stat})
   print(enemy_creature_dictionary)
   repeat = str(input("Do you wanna change anything else?(yes or no)"))
   if repeat == "yes": stat_change()
   if repeat == "no": exit()


rerun = str(input("Do you wanna change anything?(yes or no)"))
if rerun == "yes": stat_change()









