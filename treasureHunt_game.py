print("Welcome to Treasure Island Your mission is to find treasure..")

go = input("Where you want to go left or right ? ")
if go == "left":
    task = input("You are come to lake , what you want to do swim or wait ? ")
    if task == "wait":
        door = input("There house of three doors , Which door red , blue , yellow ? ")
        if door == "yellow":
            print("You Win . . !")
        elif door == "red":
            print("It's room ofull of fire , Game Over . . ")
        else:
            print("You enter a room of beats , Game Over . . ")
    else:
        print("You got atacked by an angry trout , Game Over . .")
else:
    print("You fell into hole , Game Over . .")