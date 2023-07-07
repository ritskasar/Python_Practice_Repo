from random import randint

easy_turn = 10
hard_turn = 5

# function check user guess against actual answer . .  
def check_number(guess, number, turn):
    if guess > number:
        print("Too High . . ")
        return turn - 1
    elif guess < number:
        print("Too Low . .")
        return turn - 1
    else:
        print(f"You got it ! The number is {number}")

# function sets difficulty level . .    
def set_Difficulty():
    level = input("Choose a difficulty . . \nType 'easy' or 'hard' : ")
    if level == "easy":
        return easy_turn
    else:
        return hard_turn
    
def game():
    
    print("Welcome to Number Guessing Game ! ")
    print("Guess a number between from 1 to 100 . . ")
    # print(f"Correct number is {number}")

    number = randint(1, 100)

    turn = set_Difficulty()
    
    guess = 0 
    while guess != number:
        print(f"You have {turn} attempts to guess the number ")
        guess = int(input("Enter your guess number : "))
        turn = check_number(guess, number, turn)
        
        if turn == 0:
            print("You out of guesses , You Lose . . ")
            return
        elif guess != number:
            print("Guess Again . . ")
              
game()