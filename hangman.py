import random 
from words import base_words
import string

def valid_word(words):
    chosen_word = random.choice(words)
    while '-' in chosen_word or ' ' in chosen_word:
          chosen_word = random.choice(words)

    return chosen_word.upper()

print('------HANGMAN GAME------')
#user_letter = input('Welcome to the hangman game! Please insert a letter to start: ')
#while len(user_letter) > 1 or 0:
       # user_letter = input('Please insert a one valid letter!: ')

chosen_word = valid_word(base_words)
word_letters = set(chosen_word)
already_letters = set()
alpabhet = set(string.ascii_uppercase)

while len(word_letters) > 0: #and lives > 0:
    user_letter = input('Guess a letter: ').upper()
    already_letters.add(user_letter)
    print(already_letters) ####
    lives = 10 
    print(f'You have', lives, 'lives left and you have inserted these letters:', already_letters)
    if user_letter in word_letters:
         print('Congratulations!') 

    


        #user_letter = input('Please insert a one valid letter!: ')
#fazer sistema de validação sem números 



