# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P3 - Student Record Manager
# Date: November 21, 2026


# Global variables to store student records and prevent duplicates
student_records = []
student_names = set()


# Function to add a new student
def add_student():
    student_name = input("Enter student name: ").strip()

    # Check if the entered name is empty
    if student_name == "":
        print("Student name cannot be empty.")
        return

    # Convert the name to lowercase for duplicate checking
    normalized_name = student_name.lower()

    if normalized_name in student_names:
        print("Student already exists!")
    else:
        student_records.append(student_name)
        student_names.add(normalized_name)
        print(student_name, "successfully added!")


# Function to remove an existing student
def remove_student():
    student_name = input("Enter student name to remove: ").strip()

    # Search for the student without considering uppercase or lowercase
    for existing_student in student_records:
        if existing_student.lower() == student_name.lower():
            student_records.remove(existing_student)
            student_names.remove(existing_student.lower())
            print(existing_student, "successfully removed!")
            return

    print("Student not found.")


# Function to search for a student by name
def search_student():
    search_keyword = input("Enter name to search: ").strip().lower()

    if search_keyword == "":
        print("Please enter a search keyword.")
        return

    student_found = False

    # Display students whose names contain the search keyword
    for student_name in student_records:
        if search_keyword in student_name.lower():
            print("Found:", student_name)
            student_found = True

    if not student_found:
        print("No matching student found.")


# Function to display all student records alphabetically
def display_students():
    if not student_records:
        print("No student records available.")
        return

    print("\n===== STUDENT LIST =====")

    # Sort student names alphabetically
    sorted_students = sorted(student_records, key=str.lower)

    for student_number, student_name in enumerate(sorted_students, start=1):
        print(f"{student_number}. {student_name}")

    print("Total Students:", len(student_records))


# Main menu of the Student Record Manager
while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    menu_choice = input("Choose an option: ")

    if menu_choice == "1":
        add_student()

    elif menu_choice == "2":
        remove_student()

    elif menu_choice == "3":
        search_student()

    elif menu_choice == "4":
        display_students()

    elif menu_choice == "5":
        print("Thank you for using Student Record Manager!")
        break

    else:
        print("Invalid choice. Please try again.")


# Difference between List and Set:
# A list stores student names and keeps their original order.
# A set stores unique names and helps prevent duplicate entries.
# In this program, I used a list to store and display student
# records, while a set checks if a name already exists.
