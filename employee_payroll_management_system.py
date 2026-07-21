##------------ Mini Project 3 ----------------##
##------- Employee Payroll Management System -------##

# Display Header
def display_header():
    print("==============================================")
    print(" EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
    print("==============================================")


# Calculate Salary
def calculate_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    gross_salary = basic_salary + hra + da
    return hra, da, gross_salary


# Calculate Tax
def calculate_tax(gross_salary):
    if gross_salary >= 80000:
        tax = gross_salary * 0.10
    elif gross_salary >= 60000:
        tax = gross_salary * 0.05
    else:
        tax = 0
    return tax


# Calculate Net Salary
def calculate_net_salary(gross_salary, tax):
    net_salary = gross_salary - tax
    return net_salary


# Employee Grade
def employee_grade(net_salary):
    if net_salary >= 90000:
        return "A"
    elif net_salary >= 70000:
        return "B"
    elif net_salary >= 50000:
        return "C"
    else:
        return "D"


# Payroll Report
def payroll_report(name, employee_id, department,
                   basic_salary, hra, da,
                   gross_salary, tax,
                   net_salary, grade):

    print("\n==============================================")
    print("              PAYROLL REPORT")
    print("==============================================")

    print("Employee Name   :", name)
    print("Employee ID     :", employee_id)
    print("Department      :", department)

    print("----------------------------------------------")

    print("Basic Salary    :", basic_salary)
    print("HRA (20%)       :", hra)
    print("DA (10%)        :", da)
    print("Gross Salary    :", gross_salary)
    print("Tax             :", tax)
    print("Net Salary      :", net_salary)
    print("Employee Grade  :", grade)

    print("==============================================")


# Master Function
def employee_profile(name, employee_id, department, basic_salary):

    hra, da, gross_salary = calculate_salary(basic_salary)

    tax = calculate_tax(gross_salary)

    net_salary = calculate_net_salary(gross_salary, tax)

    grade = employee_grade(net_salary)

    payroll_report(
        name,
        employee_id,
        department,
        basic_salary,
        hra,
        da,
        gross_salary,
        tax,
        net_salary,
        grade
    )


# Main Program
display_header()

employee_profile(
    "Chandu",
    216363,
    "IT",
    50000
)

employee_profile(
    "Kalyan",
    216364,
    "HR",
    42000
)

employee_profile(
    "Raju",
    216365,
    "Finance",
    60000
)