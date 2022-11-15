EASY_LEVEL = 10
HARD_LEVEL = 5
from random import randint


def check_guess(guess, answer, turns): 
    """Returns the number of turns remaining and checks the answer against the guesses."""
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it right! The answer was {answer}")
        

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'. \n").lower
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    turns = difficulty()
    guess = 0
    
    
    while guess != answer:
        print(f"You have {turns} turns remaining to guess the number.")
        guess = int(input("Make a guess!\n"))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again!")


game()
