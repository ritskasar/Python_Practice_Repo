print("Welcome to PizzaHut ! ")
size = input("Enter which size you want S , M , L ? ")
add_pepperoni = input("Do you want pepperoni Y or N ? ")
extra_cheese = input("Do you want extra cheese Y or N ? ")

bill = 0
if size == "S":
    bill += 250
elif size == "M":
    bill += 300
else:
    bill += 400
    
if add_pepperoni == "Y":
    bill += 40
    
if extra_cheese == "Y":
    bill += 60
    
print(F"Your total bill is {bill}")
print("Your pizza is ready . . ") 
    
