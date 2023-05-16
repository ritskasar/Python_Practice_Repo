first_num = input("Enter first number : ")
second_num = input("Enter second number : ")
option = input("Choose any option : \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Modulo \nEnter your choice : ")

if option == '1':
    Sum = int(first_num) + int(second_num)
    print(Sum)
    
elif option == '2':
    Sub = int(first_num) - int(second_num)
    print(Sub)
    
elif option == '3': 
    Mul = int(first_num) * int(second_num)
    print(Mul)
    
elif option == '4':
    Div = int(first_num) / int(second_num)
    print(Div)
    
elif option == '5':
    Mod = int(first_num) % int(second_num)
    print(Mod)
  
else:
    print("Wrong choise....")
    
print("Thank You !!")