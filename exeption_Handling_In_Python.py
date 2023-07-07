#  exeption handling using try-catch

num1 = input("Enter any number : ")
num2 = input("Enter any other number : ")

try:
    print("resource open")
    print(f"Division of two numbers : {num1 /num2}")
    
except ZeroDivisionError as e:
    print("You can not divide number by zero . . ", e)

except Exception as e:
    print("Invalid Input . .")
     
except Exception as e:
    print("Something went wrong . . ")
    
finally:
    print("resourse closed")