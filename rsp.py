import random
comp = [1,2,3]
quit_number = int()
string = str()
while quit_number < 10:
  is_input_correct = string in ["rock","paper", "scissors"]
  if is_input_correct == False:
    string = input("only input rock, paper or scissors: ")
  else:
    computer_hand = random.choice(comp)
    print("your hand is " + string)
    dict_player = {"rock": 1, "paper": 2, "scissors": 3}
    player_hand = dict_player[string]
    dict_computer = {1:"rock", 2:"paper", 3:"scissors"}
    test = player_hand - computer_hand
    if test < 0:
      test = test + 3         
    if test == 0:
      print("computer hand is:" + str(dict_computer[computer_hand]))
      print("draw")
      quit_number = 5
      string = input("input rock, paper or scissors: ")
    elif test == 1:
      print("computer hand is:" + str(dict_computer[computer_hand]))
      print("you win")
      quit_number = 15
    else:               
      print("computer hand is:" + str(dict_computer[computer_hand]))
      print("you lose")
      quit_number = 15
print('End')
# rock,paper,scissors 以外入力されたときを考える。if文を使う。
