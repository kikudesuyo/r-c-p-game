from util import display_input, display_result, get_winner

winner = None
while not winner:
    hand_list = display_input()
    player_hand = hand_list[0]
    opponent_hand = hand_list[1]
    winner = get_winner(player_hand, opponent_hand)
    display_result(winner)
