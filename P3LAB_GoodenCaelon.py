#Caelon Gooden
#03/24/2025
#P3LAB1
#
#Get value from user
change = float(input("Enter an amount of money: $"))

#Converting the value to an integer
change = round (change * 100)

#Determine how many dollars/coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

number_quarters = change // 25
change = change - (number_quarters * 25)

number_dimes = change // 10
change = change - (number_dimes * 10)

number_nickels = change // 5
change = change - (number_nickels * 5)

number_pennies = change

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")
if number_quarters > 0:
    if number_quarters == 1:
        print(f"{number_quarters} Quarter")
    else:
        print(f"{number_quarters} Quarters")
if number_dimes > 0:
    if number_dimes == 1:
        print(f"{number_dimes} Dime")
    else:
        print(f"{number_dimes} Dimes")
if number_nickels > 0:
    if number_nickels == 1:
        print(f"{number_nickels} Nickel")
    else:
        print(f"{number_nickels} Nickels")
if number_pennies > 0:
    if number_pennies == 1:
        print(f"{number_pennies} Penny")
    else:
        print(f"{number_pennies} Pennies")