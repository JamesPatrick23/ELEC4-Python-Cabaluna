# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# File: student_utils.py
# Date: November 21, 2026


# Function to calculate the average of student grades
def calculate_average(student_grades):
    return sum(student_grades) / len(student_grades)


# Function to determine if the student passed or failed
def get_status(student_grades):
    average_grade = calculate_average(student_grades)

    if average_grade >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function to get the highest grade
def get_highest(student_grades):
    return max(student_grades)


# Function to get the lowest grade
def get_lowest(student_grades):
    return min(student_grades)

#Explanation: We import the entire module. To use its functions, we write the module name followed by a dot and the function name.