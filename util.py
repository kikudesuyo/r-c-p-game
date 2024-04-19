import random


def get_player_hand():
    """playerの入力"""

    is_input_valid = False
    while not is_input_valid:
        hand = input("Enter rock, paper or scissors: ")
        is_input_valid = hand in ["rock", "paper", "scissors"]
    return hand


def get_opponent_hand():
    """敵の手を選ぶ"""

    random_str = ["rock", "paper", "scissors"]
    opponent_hand = random.choice(random_str)
    return opponent_hand


def get_winner(player_hand, opponent_hand):
    """勝利判定

    Return:
    winner(dic): じゃんけんの勝利判定の辞書
    difference(int): じゃんけんの判定値

    """

    hand_num_table = {"rock": 1, "paper": 2, "scissors": 3}
    player = hand_num_table[player_hand]
    opponent = hand_num_table[opponent_hand]
    difference = player - opponent if player - opponent >= 0 else player - opponent + 3
    winner = {0: None, 1: "player", 2: "opponent"}
    return winner[difference]


def display_result(winner):
    """結果の表示"""

    if winner == None:
        print("draw")
    elif winner == "player":
        print("you win")
    elif winner == "opponent":
        print("you lose")


def display_input():
    """入力する手と相手の手を表示

    Ruturn:
    hands(list): 自分と相手の手をリスト化

    """

    player_hand = get_player_hand()
    opponent_hand = get_opponent_hand()
    hands = [player_hand, opponent_hand]
    print("your hand is :" + player_hand)
    print("opponent hand is: " + opponent_hand)
    return hands
