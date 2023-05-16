age = input("Enter your age : ")

if int(age) >= 18:
    print("You are adult . . ")
    print("You are eligible to vote....") 
    
elif int(age) >= 3 and int(age) < 18:
    print("You are school student . .")
    
else:
    print("You are child now .. . ")  
    
print("Thank You !!!!")