#Caelon Gooden
# 04/16/2025
# P4HW2
# Calculate groos pay as well as total amount paid for overtime, regular pay, and payment for all employees
#Get employee name
employee_name = input("""Enter employee's name or "Done" to terminate: """)
#Create lists to store employee information
employee_list = []
overtime_list = []
regular_list = []
gross_list = []
#Create a while loop to continue until user enters "Done"
while employee_name != "Done":
    # Gather more employee information
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    hourly_rate = float(input(f"What is {employee_name}'s pay rate? "))
    # Print results given from employee
    print ("")
    print ("Employee Name:   ", employee_name)
    print ("")
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
    print (f'{hours_worked:<17}'f'{hourly_rate:<15.2f}'f'{overtime_hours:<15.1f}'f'{overtime_pay:<15.2f}$'f'{regular_pay:<15.2f}$'f'{gross_pay:.2f}')
    # Add employee information to lists
    employee_list.append(employee_name)
    overtime_list.append(overtime_pay)
    regular_list.append(regular_pay)
    gross_list.append(gross_pay)
    print("")
    # Ask user if they want to enter another employee
    employee_name = input("""Enter employee's name or "Done" to terminate: """)
else:
    print("")
    # Display information regarding all employees involved
    print("Total number of employees entered: "  + str(len(employee_list)))
    print("Total amount paid for overtime: $" + "{:.2f}".format(sum(overtime_list)))
    print("Total amount paid for regular hours: $" + "{:.2f}".format(sum(regular_list)))
    print("Total amount paid in gross: $" + "{:.2f}".format(sum(gross_list)))


