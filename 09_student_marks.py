#Student Marks Analyzer
marks = [78, 35, 56, 90, 42, 28, 67, 39]
highest_marks = marks[0]
lowest_marks = marks[0]
total = 0
passed = 0
failed = 0

for mark in marks:
    # Find highest and lowest marks
    if mark > highest_marks:
        highest_marks = mark
    if mark < lowest_marks:
        lowest_marks = mark

    # Calculate total
    total += mark

    # Count pass and fail
    if mark >= 40:
        passed += 1
    else:
        failed += 1

average = total / len(marks)

print("Marks of students:", marks)
print("Highest marks:", highest_marks)
print("Lowest marks:", lowest_marks)
print("Average marks:", average)
print("Number of students passed:", passed)
print("Number of students failed:", failed)
