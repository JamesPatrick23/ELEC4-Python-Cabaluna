
# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# File: p2_main.py
# Date: November 21, 2026

import datetime

import student_utils

from student_utils import calculate_average


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


current_time = datetime.datetime.now()

print("\n===== STUDENT GRADE RESULTS =====")

print("Date and Time:", current_time.strftime("%B %d, %Y %I:%M %p"))

print("Grades:", grades)

print("Average:", calculate_average(grades))
print("Status:", student_utils.get_status(grades))
print("Highest Grade:", student_utils.get_highest(grades))
print("Lowest Grade:", student_utils.get_lowest(grades))

print("\nReport generated successfully!")

#Explanation: We import the entire module. To use its functions, we write the module name followed by a dot and the function name.