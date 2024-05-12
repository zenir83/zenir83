import random
import load_dictionary
import string

word_list = load_dictionary.load('dictionary.txt') #load dictionary to choose from
computer_choice = random.choice(word_list) #random select a word from dictionary by the computer

def hangman():
    word = computer_choice
    word_letters = set(computer_choice) # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what user has guessed
    
    #get user input
    while len(word_letters) > 0:
        #letters used
        #' '.join(['a', 'b', 'c'] -> a b c)
        print('You already used these letters: ', ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You already used that character. Please try again')
        else:
            print('invalid character. Please try again')

    #gets here when len(word_letters) == 0