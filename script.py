# Importing required libraries and files
import random
import string

from word_list import words

# Code which allows the computer to select a **random** word 
# from the imported word list (word_list)

def get_valid_word(word_list):
    # The code will randomly select a word from the imported word list
    word = random.choice(words) 
    
    # Dashes and spaces are unintuitive guesses, so the function will 
    # use a conditional to filter out any randomly selected words that
    # contain dashes or spaces
    
    if '-' in word or ' ' in word:
        word = random.choice(words)
   

    return word.upper()

def hangman_game():
    # Invoking function to select the game word
    word = get_valid_word(words)

    # Creating a set of letters are valid guesses
    alphabet = set(string.ascii_uppercase) 
    
    # Creating a letter bank of guessed letters
    used_letters = set()

    # Creating a set in order to track correctly guessed letters
    letters_in_word = set(word)
    
    # -----------------------------------


    # Introduction Prompt
    user_input = input('Welcome to Python Hangman. Type "Start" \n').upper()
    if user_input == "START":
        print("YEAH! Let's get started \n ----------------------\n")
    
    # ---------------------------------------------------------------

    # Defining A Penalty
    lives = 5

    # Code that allows the user to repeatedly make a guess
    while len(letters_in_word) > 0 and lives > 0:

        # Display of the status of the game
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Your Lives: {}'.format(lives))
        print('The word: ' + ' '.join(word_list))

        # User Input: The user is prompted to guess a letter
        user_guess = input('\nGuess A Letter: ').upper()

        # Logic to determine if guess is correct or not
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in letters_in_word:
                letters_in_word.remove(user_guess)
                print('')
            else: 
                lives -= 1
                if lives == 0:
                    print("You lost. The word was {}".format(word))
                    return
                else:
                    print("\n-----------------------\nWRONG! You lost a life")
        elif user_guess in used_letters:
            print("\nYou've guessed that letter already")
        else:
            print('\nError: Invalid Character! Guess again')
        
        print("Letters guessed: " + ' '.join(used_letters))

    if lives > 0 and len(letters_in_word) == 0:
        print("Yeah You Won. You guessed {}".format(word))

hangman_game()
