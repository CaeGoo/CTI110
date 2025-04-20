# Caelon Gooden
# 4/1/2025
#P3HW2
# Calculate the salary of an employee based on their hours worked and hourly rate.

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
hourly_rate = float(input("Enter employees pay rate: "))
# Print results given from employee
print ("-------------------------------------")
print ("Employee Name: ", employee_name)
print ("Hours Worked     Pay Rate     Overtime     Overtime Pay     RegHour Pay     Gross Pay")
print ("--------------------------------------------------------------------------------------------------")
# Determine pay based on hours worked
# If hours worked is less than or equal to 40, display regular pay
# If hours worked is greater than 40, display overtime pay and regular pay
if hours_worked <= 40:
    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked
    regular_pay = regular_hours * hourly_rate
    gross_pay = regular_pay
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    regular_hours = 40
    regular_pay = regular_hours * hourly_rate
    gross_pay = regular_pay + overtime_pay
# Display results showing employee's information
print (f'{hours_worked:<17}{hourly_rate:<15}{overtime_hours:<15}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:.2f}')