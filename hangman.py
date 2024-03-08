import random 
from words import base_words
from hangman_visual import gallows_visual
import string

def valid_word(words):
    chosen_word = random.choice(words)
    while '-' in chosen_word or ' ' in chosen_word:
          chosen_word = random.choice(words)

    return chosen_word.upper()

print('------HANGMAN GAME------')


chosen_word = valid_word(base_words)
word_letters = set(chosen_word)
already_letters = set()
alphabet = set(string.ascii_uppercase)
lives = 6
print(gallows_visual[lives])

while len(word_letters) > 0 and lives > 0:
    user_letter = input('Guess a letter: ').upper()
    print(f'Already used letters: {already_letters}')
    #system to hide and show the correct letters
    word_list = [letter if letter in already_letters else '-' for letter in chosen_word] 
    print('Current word: ', ' '.join(word_list))
    if user_letter in already_letters:
         print('You have already  used that character! Please try again: ')
         print(gallows_visual[lives])
    elif user_letter in word_letters:
         print('Congratulations! You guessed correctly the letter!')
         print(gallows_visual[lives]) 
         already_letters.add(user_letter)
         word_letters.remove(user_letter)
    elif user_letter not in already_letters:
         lives = lives - 1
         if lives == 0:
               print('WRONG CHARACTER!')
               break
         print(f'Wrong character!! Now you have {lives} lives remaining ')
         print(gallows_visual[lives])
         already_letters.add(user_letter)
    
    elif user_letter not in alphabet: #fazer posteriormente um sistema de validacao de caracteres para excluir numeros e letras enviadas em conjunto
         print('This is not a valid character! please try again!!')

if lives > 0:
     print(f'You guessed the word!! It`s: {chosen_word}!!')    
elif lives == 0:
    print(f'You have wasted all your lives :c, the word was: {chosen_word}')




