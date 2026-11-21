
# Name: Your Full Name
# Section: IV-BSIT
# Activity: P2 - Custom Module
# File: student_utils.py
# Date: November 21, 2026

# Function 1: Calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 2: Determine pass or fail
def get_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 3: Get the highest grade
def get_highest(grades):
    return max(grades)


# Function 4: Get the lowest grade
def get_lowest(grades):
    return min(grades)

#Explanation: We import the entire module. To use its functions, we write the module name followed by a dot and the function name.