# Automatic Password generator . . 

import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
             'w', 'x', 'y', 'z'
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
             'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
             'W', 'X', 'Y', 'Z'
             ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '+', '/', '|']

print("Welcome to password Generator ! ")

total_Alpha = int(input("How many letters would you like in your password : \n"))
total_Num = int(input("How many numbers would you like in your password : \n"))
total_Sym = int(input("How many symbols would you like in your password : \n"))


password_List = []  # empty list

# using random choice method . . 
for letters in range(1, total_Alpha + 1):
    password_List += random.choice(alphabets)
    
for num in range(1, total_Num + 1):
    password_List += random.choice(numbers)
    
for symbls in range(1, total_Sym + 1):
    password_List += random.choice(symbols)    
  
# easy method . .
  
password = ""
for lettter in password_List:
    password += lettter
    
print(f"Your password : {password}")

# hard method  . . .

# random shuffle method use . .   
random.shuffle(password_List)
print(password_List)

# converting password list to single word . .
password = ""
for lettter in password_List:
    password += lettter
    
print(f"Your password : {password}")