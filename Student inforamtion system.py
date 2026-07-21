###----------- MINI PROJECT 2 : STUDENT INFORMATION SYSTEM -----------###

# Function to display student profile
def student_profile(name, age, city, course, python_marks, sql_marks):
    print("\n==============================")
    print("      STUDENT PROFILE")
    print("==============================")
    print("Name         :", name)
    print("Age          :", age)
    print("City         :", city)
    print("Course       :", course)

    # Calling other functions
    calculate_marks(python_marks, sql_marks)
    calculate_percentage(python_marks, sql_marks)
    calculate_grades(python_marks, sql_marks)
    calculate_results(python_marks, sql_marks)


# Function to calculate marks
def calculate_marks(python_marks, sql_marks):
    total_marks = python_marks + sql_marks

    print("Python Marks :", python_marks)
    print("SQL Marks    :", sql_marks)
    print("Total Marks  :", total_marks)


# Function to calculate percentage
def calculate_percentage(python_marks, sql_marks):
    total_marks = python_marks + sql_marks
    percentage = (total_marks / 200) * 100

    print("Percentage   :", percentage, "%")


# Function to calculate grade
def calculate_grades(python_marks, sql_marks):
    total_marks = python_marks + sql_marks

    if total_marks >= 180:
        print("Grade        : A")
    elif total_marks >= 160:
        print("Grade        : B")
    elif total_marks >= 140:
        print("Grade        : C")
    elif total_marks >= 120:
        print("Grade        : D")
    else:
        print("Grade        : Fail")


# Function to calculate result
def calculate_results(python_marks, sql_marks):
    if python_marks >= 35 and sql_marks >= 35:
        print("Result       : PASS")
    else:
        print("Result       : FAIL")


# Main Program
print("==============================")
print(" STUDENT INFORMATION SYSTEM")
print("==============================")

student_profile("Chandu", 21, "Nagullanka", "B.Tech IT", 95, 85)
student_profile("Kalyan", 24, "Hyderabad", "B.Tech CSE", 85, 75)
student_profile("Chiru", 27, "Vizag", "B.Tech CSM", 55, 95)