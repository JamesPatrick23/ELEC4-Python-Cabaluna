
# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# File: p2_main.py
# Date: November 21, 2026

import datetime
import student_utils

from student_utils import calculate_average


# Display the student grade report title
print("===== STUDENT GRADE REPORT =====")


# Ask how many grades the user wants to enter
while True:
    try:
        number_of_grades = int(input("How many grades? "))

        if number_of_grades > 0:
            break
        else:
            print("Please enter at least one grade.")

    except ValueError:
        print("Invalid input. Enter a whole number.")


# Store the entered grades in a list
student_grades = []

for grade_number in range(number_of_grades):

    while True:
        try:
            entered_grade = float(
                input(f"Enter grade {grade_number + 1}: ")
            )

            # Validate that the grade is between 0 and 100
            if 0 <= entered_grade <= 100:
                student_grades.append(entered_grade)
                break
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")


# Get the current date and time
current_time = datetime.datetime.now()


# Display the calculated student results
print("\n===== STUDENT GRADE RESULTS =====")

print("Date and Time:", current_time.strftime("%B %d, %Y %I:%M %p"))

print("Grades:", student_grades)

# Use functions from the custom module to calculate results
print("Average:", calculate_average(student_grades))
print("Status:", student_utils.get_status(student_grades))
print("Highest Grade:", student_utils.get_highest(student_grades))
print("Lowest Grade:", student_utils.get_lowest(student_grades))

print("\nReport generated successfully!")


# Explanation:
# We import the entire student_utils module using import student_utils.
# To access its functions, we use the module name followed by a dot.
# We also import calculate_average directly, allowing us to call
# that function without writing the module name.
