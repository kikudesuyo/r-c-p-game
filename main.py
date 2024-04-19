from util import display_input, display_result, judge_winner

winner = None
while not winner:
    player_hand, opponent_hand = display_input()
    winner = judge_winner(player_hand, opponent_hand)
    display_result(winner)
