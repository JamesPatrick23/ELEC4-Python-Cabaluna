
# Name: James Patrick Cabaluna
# Section: IV-BSIT-C
# Activity: P4 - Safe Menu Program
# Date: November 21, 2026


# Function to safely divide two numbers
def divide_numbers():
    print("\n===== DIVISION =====")

    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        # Perform division
        result = first_number / second_number

    except ValueError:
        # Handle invalid number input
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")

    else:
        # Display the result if no error occurs
        print("Result:", result)

    finally:
        # This message always appears
        print("Division operation finished.")


# Function to safely open and read a file
def open_file():
    print("\n===== OPEN FILE =====")

    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as opened_file:
            file_content = opened_file.read()

    except FileNotFoundError:
        # Handle missing files
        print("Error: File does not exist.")

    else:
        # Display file contents if the file opens successfully
        print("\n===== FILE CONTENTS =====")
        print(file_content)

    finally:
        # This message always appears
        print("File operation finished.")


# Main menu loop
while True:
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

    menu_choice = input("Choose an option: ")

    if menu_choice == "1":
        divide_numbers()

    elif menu_choice == "2":
        open_file()

    elif menu_choice == "3":
        print("Thank you for using Safe Menu Program!")
        break

    else:
        print("Invalid menu choice. Please select 1, 2, or 3.")
