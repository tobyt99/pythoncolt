from random import choice, randint
player_wins = 0
computer_wins = 0
winning_score = 5

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} R2D2 Score: {computer_wins}")
    player = input("Make your selection...\n...Rock... \n...Paper...\n...Scissors...\n").lower()
    if player == "q":
        break
    machine = choice(["rock", "paper", "scissors"]) 
    print(f"R2D2 chose {machine} ")
    if player == "rock" or player == "paper" or player == "scissors":    
        if player == machine:
            print(f"It's a draw {player} and {machine} are the same - play agin")
        elif player == "rock" and machine == "scissors":
            print(f"You won {player} beats {machine} every time!")
            player_wins += 1
        elif player == "scissors" and machine == "paper":
            print(f"You won {player} beats {machine} every time!")
            player_wins += 1
        elif player == "paper" and machine == "rock":
            print(f"You won {player} beats {machine} every time!")
            player_wins += 1
        else:
            print(f"unlucky you lost {machine} beats {player} sorry!")
            computer_wins += 1
    else: 
        print(f"you chose '{player}' which isn't part of the game - please choose a proper weapon...")
print(f"FINAL SCORE = you: {player_wins} R2D2: {computer_wins}")        