from controller import Opponent, Result, User


class View:
    def input_hand(self):
        hand = input("Enter rock , paper or scissors:")
        print("")
        return hand

    def create_user(self):
        return User(self.input_hand())

    def start_game(self):
        print("Good Luck\n")
        user = self.create_user()
        opponent = Opponent()
        print(f"{opponent.hand.__class__.__name__}\n")
        rule = Result()
        print(f"{rule.judge(user.hand, opponent.hand)}\n")
        print("End")
