# Rock paper scissors game using Python

import random

def get_choices():
    """ Gets the choices of both the player and the computer. """
    player_choice = input("Enter your choice (rock,paper,scissors):").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices


def check_win(player,computer):
    """ Tells us who won the game. """
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You lose!"
        else:
            return "Paper covers rock! You win!"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
