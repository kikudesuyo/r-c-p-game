from util import display_input, display_result, get_winner

winner = None
while not winner:
    player_hand, opponent_hand = display_input()
    winner = get_winner(player_hand, opponent_hand)
    display_result(winner)
