import os

def add(num1, num2):
    """Addition of two number . . """
    return num1 + num2

def sub(num1, num2):
    """Substraction of two number. . """
    return num1 - num2

def mul(num1, num2):
    """Multiplication of two number"""
    return num1 * num2

def div(num1, num2):
    """Division of two number . . """
    return num1 / num2

# dictionary for operations . . 
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

isContinue = True

while isContinue:
    
    num1 = float(input("Enter a number : "))
    num2 = float(input("Enter number : "))

    for symbols in operations:
        print(symbols)
    choice = input("Enter which function you like to do : \n")
    
    if choice == '+':
        ans = add(num1, num2)
    elif choice == '-':
        ans = sub(num1, num2)
    elif choice == '*':
        ans = mul(num1, num2)
    elif choice == '/':
        ans = div(num1, num2)
    else:
        print("Wrong choice . . .")
    
    print(f"{num1} {choice} {num2} = {ans}")
    
    should_continue = input("Are there any other calculations ? 'yes' or 'no' ")
    if should_continue == 'no':
        isContinue = False
    elif should_continue == 'yes':
        os.system('cls') 

