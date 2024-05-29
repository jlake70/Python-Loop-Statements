# Task 1

game_items = ['gun', 'knife', 'sword', 'bomb']

import random

item_selected = random.choice(game_items)

for item in game_items:
   player = input("What item are you selecting: ")
   if item == item_selected:
    print("You guessed correctly!") 
    
   else:
     if item != item_selected:
       print("Restart the game and try again!")

    