##==============================================##
##             MINI PROJECT 7
##      STUDENT PERFORMANCE MANAGEMENT SYSTEM
##==============================================##

def display_header():
    print("=" * 50)
    print("      STUDENT PERFORMANCE MANAGEMENT SYSTEM")
    print("=" * 50)


def calculate_total(*marks):
    total = 0

    for mark in marks:
        total += mark

    number_of_subjects = len(marks)
    return total, number_of_subjects


def calculate_average(total, number_of_subjects):
    average = total / number_of_subjects
    return average


def calculate_grade(average):
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "Fail"

    return grade


def student_report(student_id, *marks, **details):

    print("\n========== STUDENT REPORT ==========")

    print("Student ID       :", student_id)

    for key, value in details.items():
        print(f"{key.capitalize():16}: {value}")

    print("Marks            :", marks)

    total, subjects = calculate_total(*marks)
    average = calculate_average(total, subjects)
    grade = calculate_grade(average)

    print("Total Marks      :", total)
    print("No. of Subjects  :", subjects)
    print("Average Marks    :", round(average, 2))
    print("Grade            :", grade)

    print("=" * 35)


# Main Program
display_header()

student_report(
    101,
    90, 85, 88, 92, 95,
    name="Chandu",
    age=21,
    branch="IT",
    semester="4th",
    college="Aditya University"
)

student_report(
    103,
    90, 75, 88, 65, 95,
    name="Raju",
    age=23,
    branch="CSE",
    semester="5th",
    college="Aditya Enginnering College"
)

student_report(
    105,
    80, 75, 80, 65, 95,
    name="Raju",
    age=25,
    branch="ECE",
    semester="6th",
    college="Aditya University"
)
