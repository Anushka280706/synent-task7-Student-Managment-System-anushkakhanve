import json
import os

FILE_NAME = "students.json"

# Load data from JSON file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to JSON file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add student
def add_student():
    students = load_students()

    student = {
        "id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "age": input("Enter Age: "),
        "course": input("Enter Course: ")
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")

# View students
def view_students():
    students = load_students()

    if not students:
        print("No records found.")
        return

    print("\nStudent Records:")
    for student in students:
        print(student)

# Update student
def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            student["course"] = input("New Course: ")

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")

# Delete student
def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ")

    updated_list = [student for student in students if student["id"] != student_id]

    if len(updated_list) == len(students):
        print("Student not found.")
    else:
        save_students(updated_list)
        print("Student deleted successfully!")

# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")