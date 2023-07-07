import random

print("Welcome player_1")
choice = int(input("What do you choose ? 0 , 1 , 2\n"))
rock = "✊"
paper = "✋"
scissors = "✌️"


if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
    
computer_Choice = random.randint(0, 2)
print(f"Computer Choice {computer_Choice}\n")
if computer_Choice == 0:
    print(rock)
elif computer_Choice == 1:
    print(paper)
elif computer_Choice == 2:
    print(scissors)
  
if choice >= 3 or computer_Choice >= 3:
    print("default choice . . 😢")
elif choice > computer_Choice:
    print("Player_1 Win ..! 🎉✨")
elif choice == 2 and computer_Choice == 0:
    print("Player_1 Lose..! 😢😭")
elif computer_Choice == 2 and choice == 0:
    print("Player_2 lose..!😢😭")
elif computer_Choice > choice:
    print("Player_2 Win ..!🎉✨")
elif computer_Choice == choice:
    print("It's a draw")
