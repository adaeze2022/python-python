import random
rock = '''
    ___________
___'    (______)
        (______)
        (______)
        (____)
---.__ (___)
'''

paper = '''
     ________
___'   ______)____
        __________)
        ___________)
         _________)
---._________)
'''        

scissors = '''
    _________
---'    _____)___
         ________)
     ____________)
     (____)
---._(___)
'''

print("ROCK! PAPER! SCISSORS!")
game_images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0:
    print("You have entered an invalid number! You lose!")
else:
    print(game_images[player_choice])
    AI_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[AI_choice])
if player_choice == 0 and AI_choice == 2:
    print("You Win!")
elif player_choice == 2 and AI_choice == 0:
    print("You lose!")
elif player_choice > AI_choice:
    print("You Win!")
elif player_choice < AI_choice:
    print("You lose!")
elif player_choice == AI_choice:
    print("It's a draw!")
