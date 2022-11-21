import random
from util import is_player_hand

comp = [1,2,3]
quit_string = "continue"
string = str()
while quit_string == "continue":
  is_input_correct = string in ["rock","paper", "scissors"]
  if is_input_correct == False:
    string = input("only input rock, paper or scissors: ")
  else:
    computer_hand = random.choice(comp)
    print("your hand is " + string)
    dict_player = {"rock": 1, "paper": 2, "scissors": 3}
    player_hand = dict_player[string]
    dict_computer = {1:"rock", 2:"paper", 3:"scissors"}
    result = player_hand - computer_hand
    if result < 0:
      result = result + 3
    if result == 0:
      print("computer hand is:" + str(dict_computer[computer_hand]))
      print("draw")
      quit_string = "continue"
      string = input("input rock, paper or scissors: ")
    elif result == 1:
      print("computer hand is:" + str(dict_computer[computer_hand]))
      print("you win")
      quit_string = "quit"
    else:
      print("computer hand is:" + str(dict_computer[computer_hand]))
      print("you lose")
      quit_string = "quit"
print('End')

# playerの入力
# 相手の手を選ぶ
# 勝利判定
# 結果の表示