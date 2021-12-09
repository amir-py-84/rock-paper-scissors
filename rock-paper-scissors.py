import random

print("Rock...".lower())
print("Paper...".lower())
print("Scissors...".lower())
print("------------------")

randomNumber = random.randint(0, 2)
computerMove = "rock"

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"

player1_wins = 0
player2_wins = 0
winning_score = 4

while player1_wins < winning_score and player2_wins < winning_score:
    print(f"player1 :{player1_wins} and player2 :{player2_wins}")
    player_1 = input("player_1 make your move:")
    print(f"player_2 make your move: {computerMove}")
    player_2 = computerMove
    if player_1 =="q" or player_1 == "quit" :
        break
        
    if player_1 == player_2 :
        print("thats a tie")
    elif player_1 == "rock":
        if player_2 == "paper":
            print("player_2 wins!...")
            player2_wins +=1
        elif player_2 =="scissors":
            print("player_1 wins!..")
            player1_wins+=1
    elif player_1=="paper":
        if player_2 == "scissors":
            print("player_2 wins!...")
            player2_wins +=1
        elif player_2 == "rock":
            print("player_1 wins!..")
            player1_wins +=1
    elif player_1=="scissors":
        if player_2 =="rock":
           print("player_2 wins!..")
           player2_wins+=1
        if player_2 == "paper":
            print("player_1 wins!..")
            player1_wins +=1
    else:
        print("something went wrong ....")


print(f"Final Scores: player 1 : {player1_wins} | player 2 : {player2_wins}")
        
