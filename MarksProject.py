name = input("What is your name?")
total_marks = float(input("How many total marks?"))
obtained_marks = float(input("How many marks were obtained?"))

def percentage(total, obtained):
    return obtained / total * 100

result = percentage(total_marks, obtained_marks)
print(result)
