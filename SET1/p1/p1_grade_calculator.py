# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

# Global variable to store all student grades
student_grades = []


# Function to enter and validate student grades
def enter_grades():
    student_grades.clear()

    number_of_grades = int(input("How many grades? "))

    for grade_number in range(number_of_grades):
        while True:
            try:
                entered_grade = float(
                    input(f"Enter grade {grade_number + 1}: ")
                )

                # Check if the grade is within the valid range
                if 0 <= entered_grade <= 100:
                    student_grades.append(entered_grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid input. Enter a number.")


# Function to calculate the average of all grades
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function to get the highest grade
def get_highest_grade(grades):
    return max(grades)


# Function to get the lowest grade
def get_lowest_grade(grades):
    return min(grades)


# Function to determine if the student passed or failed
def get_student_status(grades):
    average_grade = calculate_average(grades)

    if average_grade >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function to display the student results
def show_results():
    if not student_grades:
        print("Please enter grades first.")
        return

    print("\n===== STUDENT RESULTS =====")
    print("Grades:", student_grades)
    print("Average:", calculate_average(student_grades))
    print("Highest:", get_highest_grade(student_grades))
    print("Lowest:", get_lowest_grade(student_grades))
    print("Status:", get_student_status(student_grades))


# Main menu of the Student Grade Calculator
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
        print("Thank you for using Grade Calculator!")
        break

    else:
        print("Invalid choice. Try again.")


# Local and Global Variables:
# The grades variable is global because it is declared
# outside the functions. It can be accessed by different
# functions in this program. Variables such as grade and
# average are local because they are declared inside functions.
