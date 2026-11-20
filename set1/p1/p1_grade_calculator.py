
# Full Name: Maricris Panuyas
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator

def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("How many grades? "))

            if count <= 0:
                print("Please enter at least one grade.")
                continue

            break

        except ValueError:
            print("Invalid input. Enter a whole number.")

    for i in range(count):
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

    return grades


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


def main():
    grades = []

    print("Name: MARICRIS PANUYAS")
    print("Section: IV-BSITC")

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")


        choice = input("Choose an option: ")

        if choice == "1":
            grades = enter_grades()
            print("Grades saved successfully!")

        elif choice == "2":
            if not grades:
                print("Please enter grades first.")
            else:
                print("\n===== GRADE RESULTS =====")
                print(f"Average: {calculate_average(grades):.2f}")
                print(f"Highest: {get_highest(grades):.2f}")
                print(f"Lowest: {get_lowest(grades):.2f}")
                print(f"Status: {get_status(grades)}")

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()



# A local variable is created inside a function.
# In my program, grades is a local variable inside main().
# A global variable is created outside of functions and
# can be used by other functions in the program.
# I used local variables to keep my code organized.

