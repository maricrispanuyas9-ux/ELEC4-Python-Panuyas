
# Full Name: MARICRIS PANUYAS
# Section: IV-BSITC
# Activity: P4 - Safe Menu Program


from pathlib import Path

def divide_numbers():
    print("\n===== DIVISION CALCULATOR =====")

    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        result = first / second

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Division Result: {result:.2f}")

    finally:
        print("Division operation completed.")


def open_file():
    print("\n===== OPEN FILE =====")

    filename = input("Enter file name: ").strip()

    try:
        
        file_path = Path(__file__).parent / filename

        with open(file_path, "r", encoding="utf-8") as file:
            contents = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except OSError as error:
        print(f"Error opening file: {error}")

    else:
        print("\n===== FILE CONTENTS =====")
        print(contents)

    finally:
        print("File operation completed.")

def main():
    print("===================================")
    print("SAFE MENU PROGRAM")
    print("Name: MARICRIS PANUYAS")
    print("Section: IV-BSITC")
    print("===================================")

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Divide Two Numbers")
        print("2. Open a File")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()
