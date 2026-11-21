
# Name: James Patrick Cabaluna
# Section: IV-BSIT
# Activity: P3 - Student Record Manager
# Date: November 21, 2026

# List stores the original student names
students = []

# Set prevents duplicate names
student_names = set()


# Function 1: Add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    # Convert name to lowercase for duplicate checking
    normalized_name = name.lower()

    if normalized_name in student_names:
        print("Student already exists!")
    else:
        students.append(name)
        student_names.add(normalized_name)
        print(name, "successfully added!")


# Function 2: Remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_names.remove(student.lower())
            print(student, "successfully removed!")
            return

    print("Student not found.")


# Function 3: Search for a student
def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    if keyword == "":
        print("Please enter a search keyword.")
        return

    found = False

    for student in students:
        if keyword in student.lower():
            print("Found:", student)
            found = True

    if not found:
        print("No matching student found.")


# Function 4: Display all students
def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n===== STUDENT LIST =====")

    sorted_students = sorted(students, key=str.lower)

    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    print("Total Students:", len(students))


# Main menu
while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you for using Student Record Manager!")
        break

    else:
        print("Invalid choice. Please try again.")


# Difference between List and Set:
# A list stores student names and keeps their original order.
# A set stores unique names and helps prevent duplicate entries.
# In this program, I used a list to store and display student
# records, while a set checks if a name already exists.
