import random
player1 = 0
player2 = 0


N=5
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

for i in range(N) :
        player1 += random.choice(dice1)
        player2 += random.choice(dice2)
        
if player1>player2:
    print(f"player1 had {player1/N} average")
elif player1<player2:
    print(f"player2 had {player2/N} average")
else :
    print(f"Draw {player1/N}")
