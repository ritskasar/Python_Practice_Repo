student_Score = input("Enter list of student score : ").split()

for n in range(0, len(student_Score)):
    student_Score[n] = int(student_Score[n])
    
print(student_Score)
highest_Score = 0
for scores in student_Score:
    if scores > highest_Score:
        highest_Score = scores
print(f"Highest score in class is {highest_Score}")