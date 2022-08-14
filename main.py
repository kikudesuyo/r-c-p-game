hand = { "r" : 1, "s" : 2, "p" : 3 }


player = input("r or s or p") 
player = hand[player]

opponent = 2
if player > opponent:
    print("You win.")
else:
    print("You may lose")
    

