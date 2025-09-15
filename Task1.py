# rock_paper_scissors.py
#  I started this work by searching online on how to play the game
#  i computed each action with a function
#  then i use the if elif else to make decision
#  And while loop for looping base on my decision

import random

CHOICES = ["rock", "paper", "scissors"]
WINS_AGAINST = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def get_user_choice():
    choice = input("Choose (rock/paper/scissors): ").strip().lower()
    while choice not in CHOICES:
        print("Invalid choice. Try again.")
        choice = input("Choose (rock/paper/scissors): ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(CHOICES)

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    if WINS_AGAINST[user] == computer:
        return "user"
    return "computer"

def main():
    user = get_user_choice()
    computer = get_computer_choice()
    result = decide_winner(user, computer)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print(f"{user.capitalize()} beats {computer} — you win!")
    else:
        print(f"{computer.capitalize()} beats {user} — computer wins!")


if __name__ == "__main__":
     main()

