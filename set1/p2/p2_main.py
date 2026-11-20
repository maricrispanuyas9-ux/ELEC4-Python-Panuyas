
# Full Name: MARICRIS PANUYAS
# Section: IV-BSITC
# Activity: P2 - Custom Module: student_utils

import student_utils

from student_utils import get_status

from datetime import datetime

def main():
    print("===================================")
    print("STUDENT GRADE REPORT")
    print("Name: MARICRIS PANUYAS")
    print("Section: IV-BSITC")
    print("===================================")

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

    
    average = student_utils.calculate_average(grades)
    highest = student_utils.get_highest(grades)
    lowest = student_utils.get_lowest(grades)
    status = get_status(grades)

    
    report_date = datetime.now()

    
    print("\n===== STUDENT GRADE REPORT =====")
    print("Name: MARICRIS PANUYAS")
    print("Section: IV-BSITC")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest:.2f}")
    print(f"Lowest: {lowest:.2f}")
    print(f"Status: {status}")
    print("Report Generated:",
          report_date.strftime("%B %d, %Y - %I:%M %p"))


if __name__ == "__main__":
    main()
