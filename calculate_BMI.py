weight = input("Enter your weight in kg : ")
height = input("Enter your height in meters : ")

BMI = int(weight) / float(height) ** 2

print("Your body mass index BMI : " + str(BMI))

if BMI < 18.5:
    print("You are underweight..")
elif BMI >= 18.5 and BMI < 25:
    print("you are normal weight..")
elif BMI >= 25 and BMI < 30:
    print("you are overweight...")
elif BMI >= 30 and BMI < 35:
    print("you are obese")
else:
    print("you are clinically obese..")