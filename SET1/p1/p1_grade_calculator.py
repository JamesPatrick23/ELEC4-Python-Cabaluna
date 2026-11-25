# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026


# Global variable to store all student grades
student_grades = []


# 1. Main Menu
def main_menu():
    while True:
        print("\n===== GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        menu_choice = input("Choose an option: ")

        if menu_choice == "1":
            enter_grades()

        elif menu_choice == "2":
            show_results()

        elif menu_choice == "3":
            print("\nThank you for using Grade Calculator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# 2. Enter and Validate Grades
def enter_grades():
    student_grades.clear()

    while True:
        try:
            number_of_grades = int(input("How many grades? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter at least 1 grade.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for grade_number in range(number_of_grades):
        while True:
            try:
                entered_grade = float(
                    input(f"Enter grade {grade_number + 1}: ")
                )

                if 0 <= entered_grade <= 100:
                    student_grades.append(entered_grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid input. Enter a number.")

    print("\nGrades successfully entered!")


# 3. Display Student Results
def show_results():
    if not student_grades:
        print("\nPlease enter grades first.")
        return

    print("\n===== STUDENT RESULTS =====")
    print("Grades:", student_grades)
    print("Average:", round(calculate_average(student_grades), 2))
    print("Highest:", get_highest_grade(student_grades))
    print("Lowest:", get_lowest_grade(student_grades))
    print("Status:", get_student_status(student_grades))


# 4. Calculate Average
def calculate_average(grades):
    return sum(grades) / len(grades)


# 5. Get Highest Grade
def get_highest_grade(grades):
    return max(grades)


# 6. Get Lowest Grade
def get_lowest_grade(grades):
    return min(grades)


# 7. Determine Student Status
def get_student_status(grades):
    average_grade = calculate_average(grades)

    if average_grade >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Run the Student Grade Calculator
main_menu()


# Local and Global Variables:
# The grades variable is global because it is declared
# outside the functions. It can be accessed by different
# functions in this program. Variables such as grade and
# average are local because they are declared inside functions.
