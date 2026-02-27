name = input("What is your name?")
total_marks = float(input("How many total marks?"))
obtained_marks = float(input("How many marks were obtained?"))

def percentage(total, obtained):
    return obtained / total * 100

result = percentage(total_marks, obtained_marks)
print(result)

if percentage(total_marks, obtained_marks) >= 80:
    grade = "A"
elif percentage(total_marks, obtained_marks) >= 70:
    grade = "B"
elif percentage(total_marks, obtained_marks) >= 60:
    grade = "C"
else:
    grade = "D"

print(grade)
