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
      
