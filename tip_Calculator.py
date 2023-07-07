print("Welcome to the Tip Calculator....")
total_Bill = float(input("What was the total bill ? $"))
tip = int(input("what percentage tip would you like to give 10, 12, 15 ? "))
group_members = int(input("How many people to split the bill ? "))

total_Amount = (tip / 100) * total_Bill + total_Bill
print("Total amount with tip : " + str(total_Amount))
split_amount = total_Amount / group_members

print("Each member should pay : $" + str(split_amount))
