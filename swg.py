# Snake_Water_Gun
#A game using python
import random
while True:
  choices=["snake","water","gun"]
  pc=random.choice(choices)
  player=None
  while player not in choices:
    player=input("snake,water,or gun?").lower()
    if player==pc:
      print("pc:",pc)
      print("player:",player)
      print("It's tie")
      elif player=="snake":
        if pc=="water":
          print("pc:",pc)
          print("player:",player)
          print("you win")
        if pc=="gun":
          print("pc:",pc)
          print("player:",player)
          print("you lose")
       elif player=="water":
        if pc=="gun":
          print("pc:",pc)
          print("player:",player)
          print("you lose")
        if pc=="snake":
          print("pc:",pc)
          print("player:",player)
          print("you win")
        elif player=="gun":
          if pc=="snake":
          print("pc:",pc)
          print("player:",player)
          print("you win")
          if pc=="water":
          print("pc:",pc)
          print("player:",player)
          print("you lose")
play_again=input("Do you want to play again?(Yes/No):").lower()
if play_again!="yes":
  break
  print("Game Over")
          
          
      
