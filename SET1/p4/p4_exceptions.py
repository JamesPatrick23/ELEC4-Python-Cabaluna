
# Name: Your Full Name
# Section: IV-BSIT
# Activity: P4 - Safe Menu Program
# Date: November 21, 2026


# Function 1: Division
def divide_numbers():
    print("\n===== DIVISION =====")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


# Function 2: Open and read a file
def open_file():
    print("\n===== OPEN FILE =====")

    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File does not exist.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)

    finally:
        print("File operation finished.")


# Main menu
while True:

    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        divide_numbers()

    elif choice == "2":
        open_file()

    elif choice == "3":
        print("Thank you for using Safe Menu Program!")
        break

    else:
        print("Invalid menu choice. Please select 1, 2, or 3.")
