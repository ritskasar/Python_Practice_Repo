# grading program using dictionary . . 

# Student score dictionary . .
student_scores = {
    "ram": 91,
    "siya": 88,
    "kisan": 81,
    "radha": 75,
    "sudama": 65,
    "arjun": 90,
    "bheem": 70,
    "dau": 60,
    "nick": 40,
    "jenne": 30,
}

# empty dictionary . .
student_grades = {}


# 
for student in student_scores:
    scores = student_scores[student]
    if scores >= 90:
        student_grades[student] = "Outstanding"
    elif scores >= 80:
        student_grades[student] = "Excelent"
    elif scores > 70:
        student_grades[student] = "good"
    elif scores >= 60:
        student_grades[student] = "acceptable"
    else:
        student_grades[student] = "fail"

        
print(student_grades)