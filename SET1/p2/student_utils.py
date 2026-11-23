
# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# File: student_utils.py
# Date: November 21, 2026

def calculate_average(grades):
    return sum(grades) / len(grades)


def get_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)

#Explanation: We import the entire module. To use its functions, we write the module name followed by a dot and the function name.