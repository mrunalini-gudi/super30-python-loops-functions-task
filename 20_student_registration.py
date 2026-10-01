# Student Registration System
students = []
marks = []
def add_student():
    """Add a new student"""
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_id = input("Enter student ID: ")
    student = {
        "name": name,
        "age": age,
        "student_id": student_id
    }
    students.append(student)
    print("Student added successfully.")

def view_students():
    """View all registered students"""
    if len(students) == 0:
        print("No students registered.")
    else:
        print("\nRegistered Students:")

        for student in students:
            print("Name of Student:", student["name"])
            print("Age of Student:", student["age"])
            print("Student ID:", student["student_id"])

def search_by_id():
    """Search for a student by ID"""
    student_id = input("Enter student ID to search: ")
    found = False
    for student in students:
        if student["student_id"] == student_id:
            print("\nStudent found:")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Student ID:", student["student_id"])
            found = True
    if not found:
        print("Student not found.")

def update_student_details():
    """Update student details"""
    student_id = input("Enter student ID to update: ")
    found = False
    for student in students:
        if student["student_id"] == student_id:
            new_name = input("Enter new name : "       )
            new_age = input( "Enter new age : ")
            if new_name != "":
                student["name"] = new_name
            if new_age != "":
                student["age"] = int(new_age)
            print("Student details updated successfully.")
            found = True
    if not found:
        print("Student not found.")
        print("Student not found.")

def delete_student():
    """Delete a student by ID"""
    student_id = input("Enter student ID to delete: ")
    found = False
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            found = True
    if not found:
        print("Student not found.")

def calculate_average_marks(marks):
    """Calculate average marks of student"""
    if len(marks) == 0:
        print("No marks available.")
        return
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    print("Class Average:", average_marks)

def highest_performing_student(marks):
    """Find the student with the highest marks"""
    if len(students) == 0:
        print("No students registered.")
        return
    if len(marks) == 0:
        print("No marks available.")
        return
    highest_marks = marks[0]
    highest_student = students[0]["name"]
    for i in range(len(marks)):
        if marks[i] > highest_marks:
            highest_marks = marks[i]
            highest_student = students[i]["name"]
    print("Highest Marks of Student:", highest_student, "is", highest_marks)

while True:
    print("\n===== Student Registration System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student by ID")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Calculate Average Marks")
    print("7. Highest Performing Student")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_by_id()
    elif choice == "4":
        update_student_details()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Enter marks for students:")
        for i in range(5):
            mark = int(input(f"Enter marks for student {i + 1}: "))
            marks.append(mark)
        calculate_average_marks(marks)
    elif choice == "7":
        highest_performing_student(marks)
    elif choice == "8":
        print("Exiting the Student Registration System.")
        break
    else:
        print("Invalid choice. Please try again.")


