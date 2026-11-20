
# Full Name: MARICRIS PANUYAS
# Section: IV-BSITC
# Activity: P3 - Student Record Manager


students = []

student_names = set()

def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    normalized_name = " ".join(name.split()).casefold()

    if normalized_name in student_names:
        print("Student already exists. Duplicate not allowed.")
    else:
        clean_name = " ".join(name.split())
        students.append(clean_name)
        student_names.add(normalized_name)
        print("Student added successfully!")

def remove_student():
    name = input("Enter student name to remove: ").strip()
    normalized_name = " ".join(name.split()).casefold()

    for student in students:
        if student.casefold() == normalized_name:
            students.remove(student)
            student_names.remove(normalized_name)
            print("Student removed successfully!")
            return

    print("Student not found.")


def search_student():
    keyword = input("Enter name to search: ").strip().casefold()

    if not keyword:
        print("Please enter a search keyword.")
        return

    matches = [
        student for student in students
        if keyword in student.casefold()
    ]

    if matches:
        print("\n===== SEARCH RESULTS =====")
        for number, student in enumerate(
            sorted(matches, key=str.casefold), 1
        ):
            print(f"{number}. {student}")
    else:
        print("No matching student found.")

def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n===== STUDENT LIST =====")

    sorted_students = sorted(students, key=str.casefold)

    for number, student in enumerate(sorted_students, 1):
        print(f"{number}. {student}")

    print(f"Total Students: {len(students)}")


def main():
    print("===================================")
    print("STUDENT RECORD MANAGER")
    print("Name: MARICRIS PANUYAS")
    print("Section: IV-BSITC")
    print("===================================")

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__":
    main()


# A list is an ordered collection that can contain duplicate
# values, while a set stores unique values without duplicates.
# In this program, the students list keeps the names entered
# by the user and allows them to be displayed alphabetically.
# The student_names set stores normalized names and checks
# whether a student already exists before adding a new one.
