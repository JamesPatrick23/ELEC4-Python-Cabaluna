
# Name: James Patrick Cabaluna
# Section: IV-BSIT
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

grades = []


def enter_grades():
    grades.clear()

    number = int(input("How many grades? "))

    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid input. Enter a number.")


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def show_results():
    if not grades:
        print("Please enter grades first.")
        return

    print("\n===== STUDENT RESULTS =====")
    print("Grades:", grades)
    print("Average:", calculate_average(grades))
    print("Highest:", get_highest(grades))
    print("Lowest:", get_lowest(grades))
    print("Status:", get_status(grades))


while True:
    print("\n===== GRADE CALCULATOR =====")
    print("1. Enter Grades")
    print("2. View Results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        enter_grades()

    elif choice == "2":
        show_results()

    elif choice == "3":
        print("Thank you for using Grade Calculator!")
        break

    else:
        print("Invalid choice. Try again.")


# Local and Global Variables:
# The grades variable is global because it is declared
# outside the functions. It can be accessed by different
# functions in this program. Variables such as grade and
# average are local because they are declared inside functions.
