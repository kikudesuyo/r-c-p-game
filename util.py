import random
  
# playerの入力
def get_player_hand():
  is_input_valid = False
  while not is_input_valid:
    hand = input("Enter rock, paper or scissors: ")
    is_input_valid = hand in ["rock", "paper","scissors"]
  return hand

# playerの手を数値に変換
def convert_playerhand_to_number():
  dict = {"rock": 1, "paper": 2, "scissors": 3}
  get_number = dict[get_player_hand()]
  return get_number
  
# 敵の手を選ぶ
def get_opponent_hand():
  random_str = ["rock", "paper", "scissors"]
  opponent_hand = random.choice(random_str)
  return opponent_hand

# 敵の手を数値に変換
def convert_oppnenthand_to_number():
  dict = {"rock": 1, "paper": 2, "scissors": 3}
  get_oppnent_number = dict[get_opponent_hand()]
  return get_oppnent_number
  
# 勝利判定
def judge_win_or_lose():
  result =  convert_playerhand_to_number() - convert_oppnenthand_to_number()
  if result < 0:
    result = result + 3
  if result == 0:
    print("computer hand is:" + str(get_opponent_hand()))
    print("draw")
    get_player_hand()
  elif result == 1:
    print("computer hand is:" + str(get_opponent_hand()))
    print("you win")
  else:
    print("computer hand is:" + str(get_opponent_hand()))
    print("you lose")
    
# 結果の表示
