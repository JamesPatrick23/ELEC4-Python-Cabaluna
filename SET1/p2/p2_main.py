
# Name: Your Full Name
# Section: IV-BSIT
# Activity: P2 - Custom Module
# File: p2_main.py
# Date: November 21, 2026

# Built-in module
import datetime

# Import style 1: Import the whole module
import student_utils

# Import style 2: Import a specific function
from student_utils import calculate_average


# Ask the user how many grades to enter
print("===== STUDENT GRADE REPORT =====")

while True:
    try:
        number = int(input("How many grades? "))

        if number > 0:
            break
        else:
            print("Please enter at least one grade.")

    except ValueError:
        print("Invalid input. Enter a whole number.")


# Store the grades in a list
grades = []

for i in range(number):

    while True:
        try:
            grade = float(input(f"Enter grade {i + 1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")


# Generate the report date and time
current_time = datetime.datetime.now()

print("\n===== STUDENT GRADE RESULTS =====")

print("Date and Time:", current_time.strftime("%B %d, %Y %I:%M %p"))

print("Grades:", grades)

# Use the imported function directly
print("Average:", calculate_average(grades))

# Use functions through the imported module
print("Status:", student_utils.get_status(grades))
print("Highest Grade:", student_utils.get_highest(grades))
print("Lowest Grade:", student_utils.get_lowest(grades))

print("\nReport generated successfully!")

#Explanation: We import the entire module. To use its functions, we write the module name followed by a dot and the function name.