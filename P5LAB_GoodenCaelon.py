#Caelon Gooden
# 04/16/2025
# P5LAB
#Using user-defined functions

import random

def disperse_change(change):

     #Converting the value to an integer
     change = round (change * 100)
     print(f"Change owed as interger: ${change}")

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
     if num_dollars == 0 and number_quarters == 0 and number_dimes == 0 and number_nickels == 0 and number_pennies == 0:
         print("No change")

def main():
    #Logic goes here

    #Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    #Create variable to represent money put into machine
    money_in = float(input("How much cash will you put into the self-checkout? "))

    #Calculate change owed to the customer
    change = money_in - amount_owed
    print(f"Change owed: ${change:.2f}")

    #Call the disperse_change function 
    disperse_change(change)

#Call the main function
main()