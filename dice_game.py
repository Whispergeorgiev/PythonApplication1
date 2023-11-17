import random

def roll_dice():
    dice_total = random.randint(1, 6)   +   random.randint(1, 6)
    return dice_total

def main():
    player1 = input("Enter player 1's name:\n")
    player2 = input("Enter player 2's name:\n")
    
    roll1 = roll_dice()
    roll2 = roll_dice()
    
    print(player1, "roled", roll1)
    print(player2, "roled", roll2)
    
    if roll1 > roll2:
        print(player1, "wins!")
        
    elif roll2 > roll1:
        print(player2, "wins!")
        
    else:
        print("TIE!")
        
main()