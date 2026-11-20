
# Full Name: MARICRIS PANUYAS
# Section: IV-BSITC
# Activity: P2 - Custom Module: student_utils

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
