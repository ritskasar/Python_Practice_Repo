import random

from hangman_Words import word_list

# randomly choose word from list . . 
chosen_word = random.choice(word_list)
print(f"Chosen word is {chosen_word}")

# creating empty list . . 
word = [] 
word_Length = len(chosen_word)
for letter in range(word_Length): 
    word += "_"
print(word)
    
# ask user to guess letter 
# end_of_game = False
i = 1
while i <= word_Length:
    guess = input("Guessa letter : ").lower()
    
    # check letter user guessed is one of letter in chosen_word
    for position in range(word_Length):
        letters = chosen_word[position]
        if letters == guess:
            word[position] = letters
    i += 1

print(word)
