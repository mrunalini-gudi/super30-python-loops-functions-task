#Student Grade Function
def calculate_grade(math: float, science: float, english: float, history: float, geography: float) -> str:
    marks = [math, science, english, history, geography]
    for mark in marks:
        if mark < 0 or mark > 100:
            return "Invalid marks. Please enter marks between 0 and 100."
    total_score = math + science + english + history + geography
    percentage = (total_score / 500) * 100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "Fail"
    return grade

math_score = float(input("Enter the math score: "))
science_score = float(input("Enter the science score: "))
english_score = float(input("Enter the English score: "))
history_score = float(input("Enter the history score: "))
geography_score = float(input("Enter the geography score: "))
print(calculate_grade(math_score, science_score, english_score, history_score, geography_score))
