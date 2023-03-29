import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_score = 0
bot_score = 0

while True:
    player_action = input("Choose [r]ock, [p]aper or [s]cissors, or press [q] to quit: ")

    if player_action == "q":
        print(f"Final score: Player {player_score} - Bot {bot_score}")
        break

    elif player_action == "r":
        player_action = rock
    elif player_action == "p":
        player_action = paper
    elif player_action == "s":
        player_action = scissors
    else:
        print("Please enter a valid input.")
        continue

    bot_number = random.randint(1, 3)
    bot_action = ""

    if bot_number == 1:
            bot_action = rock
    elif bot_number == 2:
        bot_action = paper
    else:
        bot_action = scissors

    print(f"The bot chose {bot_action}.")

    if (player_action == rock and bot_action == scissors) or \
        (player_action == paper and bot_action == rock) or \
        (player_action == scissors and bot_action == paper):
        player_score += 1
        print("You win! Congratulations!")
    elif (player_action == rock and bot_action == paper) or \
        (player_action == paper and bot_action == scissors) or \
        (player_action == scissors and bot_action == rock):
        bot_score += 1
        print("You lose! Try again!")
    else:
        print("Draw! Your move is equal to the computer's. Try again!")

    print(f"Current score: Player {player_score} - Bot {bot_score}")
