import random

person_names = ["Seokjin", "Namjoon", "Yoongi", "Houseok", "Jimin", "Taehyuong", "Jungkook"]

# random choice function . . 
person_who_pay = random.choice(person_names)

print(person_who_pay + " is going to buy the meal today ! 😀 🎉✨ ") 

# random shuffle function . .
random.shuffle(person_names)
print(person_names)
