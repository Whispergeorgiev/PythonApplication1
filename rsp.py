import random

computer_choice = random.choice(["rock", "scissors", "paper"])
user_choice = input("Do you want rock, paper or scissors:\n")

print("Computer choice:", computer_choice)

if computer_choice == user_choice:
    print("TIE")   
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win!")
else:
    print("You lose, Computer is smarter!")
    
c