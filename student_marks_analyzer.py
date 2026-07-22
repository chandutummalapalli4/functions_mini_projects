##------------🛠️ Mini Project 6 — Student Marks Analyzer -----------------##

def display_header():
    print("=" * 35)
    print("     STUDENT MARKS ANALYZER")
    print("=" * 35)


def student_report(student_name, *marks):

    total = 0
    count = 0

    highest_mark = marks[0]
    lowest_mark = marks[0]

    print("Student Name :", student_name)
    print("-" * 35)

    for mark in marks:
        print("Marks        :", mark)

        if mark > highest_mark:
            highest_mark = mark

        if mark < lowest_mark:
            lowest_mark = mark

        total += mark
        count += 1

    average = total / count

    print("-" * 35)
    print("Total Subjects :", count)
    print("Total Marks    :", total)
    print("Highest Marks  :", highest_mark)
    print("Lowest Marks   :", lowest_mark)
    print("Average        : {:.2f}".format(average))

    if average >= 90:
        print("Grade          : A")
    elif average >= 80:
        print("Grade          : B")
    elif average >= 70:
        print("Grade          : C")
    elif average >= 60:
        print("Grade          : D")
    else:
        print("Grade          : FAIL")

    print("=" * 35)
    print()


# Main Program
display_header()

student_report("Chandu", 90, 88, 77, 87, 75, 65)
student_report("Kalyan", 95, 92, 90, 94, 91)
student_report("Raju", 65, 72, 68, 70, 66)