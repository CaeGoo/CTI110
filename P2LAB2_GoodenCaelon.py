#Caelon Gooden
#P2LAB
#10/2/2023
#Using dictionaries
cars = {'Camero': 18.21 , 'Prius': 52.36, 'Model S' :110 , 'Silverado': 26}
#Get keys from dictionary
cars_keys = cars.keys()
print (cars_keys)
print(*cars_keys, sep = ', ')
#Get a car from user
car_name = input('Enter a car name: ')
# Get miles per gallon for the given car
car_mpg = cars[car_name]
print(f'The {car_name} gets {car_mpg} miles per gallon.')
# Get miles driven from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))
#Calculate 
gallons_needed = miles_driven / car_mpg
# Display results
print(f"You will need {gallons_needed:.2f} gallons of gas to drive the {car_name} {miles_driven} miles.")