import random

comp = [1,2,3]
dict_player = {"rock": 1, "paper": 2, "scissors": 3}
dict_comp = {1:"rock", 2:"paper", 3:"scissors"}
quit_flag = False
while quit_flag == False:
  computer_hand = random.choice(comp)
  print(computer_hand)
  string = input("input rock, paper or scissors: ")
  print("your hand is " + string)
  print("computer hand is:" + str(dict_comp[computer_hand]))
  player_hand = dict_player[string]
  value = (player_hand - computer_hand) % 3
  if value == 0:
    print("draw")
  elif value == 1:
    print("you win")
    quit_flag = True
  elif value == 2:
    print("you lose")
    quit_flag = True
print('End')