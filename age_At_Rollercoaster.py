print("Welcome to RollerCoaster ! ")

height = int(input("Enter your height in cm : "))

if height >= 150:
    print("You can ride the rollercoaster ! ")
    age = int(input("Enter your age : "))
    if age <= 20:
        print("pay $7")
    else:
        print("pay $10")
else:
    print("Sorry, You have to grow taller before you can ride.")
        