print("Welcome to the hangman game.")
import random
stages = ['''
   +---+
   |    |
   O    |
  /|\   |
  / \   |
        |
==========
''', '''
   +---+
   |    |
   O    |
  /|\   |
  /     |
        |
==========
''', '''
   +---+
   |    |
   O    |
  /|\   |
        |
        |
==========
''', '''
   +---+
   |    |
   O    |
  /|    |
        |
        |
==========
''', '''
   +---+
   |    |
   O    |
   |    |
        |
        |
==========
''', '''
   +---+
   |    |
   O    |
        |
        |
        |
==========
''', '''
   +---+
   |    |
        |
        |
        |
        |
==========
''']

word_list = ["ardvark", "camel", "baboon"]
chosen_word = random.choice(word_list)
lives = 6
display = []
word_length = len(chosen_word)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter!\n").lower()
    for _ in range(word_length):
        display += " _ "
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")             
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])