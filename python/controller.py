import random

from hand import Hand, Paper, Rock, Rule, Scissors


class Opponent:
    def __init__(self):
        Hand = random.choice([Rock, Scissors, Paper])
        self.hand = Hand()


class User:
    def __init__(self, string: str):
        table = {"rock": Rock, "scissors": Scissors, "paper": Paper}
        self.hand = table[string]()


class Result:

    def judge(self, user_hand: Hand, *hands: Hand):
        all_hands = [user_hand, *hands]
        rule = Rule()
        if rule.is_draw(all_hands):
            return "Draw"
        if user_hand == rule.get_winnner_hand(all_hands):
            return "Win"
        else:
            return "Lose"
