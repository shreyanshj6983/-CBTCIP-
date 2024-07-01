import random

player_input = input("Enter player choice (rock, paper, scissors): ")
actions = ["rock", "paper", "scissors"]
comp_input = random.choice(actions)
print(f"\nplayer chose {player_input}, computer chose {comp_input}.\n")

if player_input == comp_input:
    print(f"Both players selected {player_input}. It's a tie!")
elif player_input == "rock":
    if comp_input == "scissors":
        print("Rock smashes scissors! player win!")
    else:
        print("Paper covers rock! player lose.")
elif player_input == "paper":
    if comp_input == "rock":
        print("Paper covers rock! player win!")
    else:
        print("Scissors cuts paper! player lose.")
elif player_input == "scissors":
    if comp_input == "paper":
        print("Scissors cuts paper! player win!")
    else:
        print("Rock smashes scissors! player lose.")