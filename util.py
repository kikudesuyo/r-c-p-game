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
  get_number = dict.get(get_player_hand())
  return get_number
  
# 敵の手を選ぶ
def get_opponent_hand():
  number = [1,2,3]
  opponent_hand = random.choice(number)
  return opponent_hand
  
# 勝利判定

# 結果の表示
