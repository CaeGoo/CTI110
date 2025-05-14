#Caelon Gooden
# 04/092025
# P4LAB2
# Use while loop and for loop together

# Get integer from user
# Determine if integer is positive or negative
# If number is positive, display mulitplaction table
# If number is negative, tell user program can't accept it
# Ask user to run program again
# If yes, run program again
# If no, exit program 

run_again = "yes"

while run_again != "no":

    user_number = int(input("Enter an integer: "))
#display multiplication for that value and range (1-12)
    if user_number>=0:
        for item in range(1,13):
            print(f"{user_number} * {item} = {user_number*item}")
    else:
        print("This program does not handle negative numbers.")
    
    run_again = input("Would you like to run the program again?")
#Loop has broken. User has entered 'no'
print("Program is ending.....")

   