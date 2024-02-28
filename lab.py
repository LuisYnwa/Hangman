import random 
from words import base_words


def valid_word(b):
    chosen_word = random.choice(base_words)
    while '-' or ' ' in chosen_word: #ALGUM ERRO NO WHILE
          chosen_word = random.choice(base_words)
    return chosen_word.upper()
print(valid_word())