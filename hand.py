class Hand:
    def __init__(self):
        pass

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    def __hash__(self):
        return hash(self.__class__.__name__)


class Rock(Hand):
    def __init__(self):
        super().__init__()


class Scissors(Hand):
    def __init__(self):
        super().__init__()


class Paper(Hand):
    def __init__(self):
        super().__init__()


class Rule:

    def judge(self, hand: Hand, *hands: Hand):
        all_hands = [hand, *hands]
        if self.is_draw(all_hands):
            return None
        return self.get_winnner_hand(all_hands)

    def is_draw(self, hands: list[Hand]):
        types = len(set(hands))
        has_all_hands = types == 3
        is_same_hand = types == 1
        return has_all_hands or is_same_hand

    def get_winnner_hand(self, hands: list[Hand]):
        types = [type(hand) for hand in hands]
        if (Rock in types) and (Scissors in types):
            return Rock
        if (Scissors in types) and (Paper in types):
            return Scissors
        if (Paper in types) and (Rock in types):
            return Paper


unti = Rule()
print(unti.judge(Rock(), Rock()))
