import random
comp = [1,2,3]
computer_hand = random.choice(comp)
print(computer_hand)
string = input("input rock, paper or scissors: ")
print("your hand is " + string)
dict_player = {"rock": 1, "paper": 2, "scissors": 3}
player_hand = dict_player[string]
dict_comp = {1:"rock", 2:"paper", 3:"scissors"}
test = player_hand - computer_hand
if test > 0:
        test = test + 3
if test == 0:
    print("computer hand is:" + str(dict_comp[computer_hand]))
    print("draw")
elif test == 1:
        print("computer hand is:" + str(dict_comp[computer_hand]))
        print("you win")

else:               
        print("computer hand is:" + str(dict_comp[computer_hand]))
        print("you lose")