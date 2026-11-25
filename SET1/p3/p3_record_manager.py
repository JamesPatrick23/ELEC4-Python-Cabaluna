
# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P3 - Student Record Manager
# Date: November 21, 2026


# Global variables to store student records and prevent duplicates
student_records = []
student_names = set()


# 1. Main Menu
def main_menu():
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


# 2. Add Student
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


# 3. Remove Student
def remove_student():
    student_name = input("Enter student name to remove: ").strip()

    # Search without considering uppercase or lowercase
    for existing_student in student_records:
        if existing_student.lower() == student_name.lower():
            student_records.remove(existing_student)
            student_names.remove(existing_student.lower())
            print(existing_student, "successfully removed!")
            return

    print("Student not found.")


# 4. Search Student
def search_student():
    search_keyword = input("Enter name to search: ").strip().lower()

    if search_keyword == "":
        print("Please enter a search keyword.")
        return

    student_found = False

    # Display students whose names contain the keyword
    for student_name in student_records:
        if search_keyword in student_name.lower():
            print("Found:", student_name)
            student_found = True

    if not student_found:
        print("No matching student found.")


# 5. Display All Students
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


# Run the Student Record Manager
main_menu()
