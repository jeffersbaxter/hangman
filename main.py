import random
from os import system, name
from hangman_art import stages, logo 
from hangman_words import word_list

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
wrong_guesses = []
end_of_game = False
lives = 6

print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    clear()
    print(f"You have {lives} lives left")
    print(f"Wrong Guesses: {(' ').join(wrong_guesses)}")
    print(f"{' '.join(display)}")
    print(stages[lives])

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed '{guess}', guess again!")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        if guess not in wrong_guesses:
            wrong_guesses.append(guess)
        if lives == 0:
            end_of_game = True
            print(f"You lose. The correct answer was {('').join(chosen_word)}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

