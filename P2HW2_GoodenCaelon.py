#Caelon Gooden
# Date: 2/20/2021
#P2HW2
#Design a program that sum, average, max, and min of grades inputed by the user
print('Below you will enter the grades for 6 modules!')
print('In the end you will be able to see your lowest grade, highest grade, the sum of your grades, and the average of your grades!')
print('')
#User inputs grades for 6 modules
print('Enter the grade for the module 1:', end = ' ')
module_1 = float(input())
print('Enter the grade for the module 2:', end = ' ')
module_2 = float(input())
print('Enter the grade for the module 3:', end = ' ')
module_3 = float(input())
print('Enter the grade for the module 4:', end = ' ')
module_4 = float(input())
print('Enter the grade for the module 5:', end = ' ')
module_5 = float(input()) 
print('Enter the grade for the module 6:', end = ' ')
module_6 = float(input())
print('')
#Calculates the sum, average, max, and min of the grades
module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]
num_list = len(module_grades)
min_num = min (module_grades)
max_num = max (module_grades)
sum = sum(module_grades)
average = sum / num_list
#Displays the results
print('------------Results------------')
print(f'{'Lowest grade:':<20} {min_num:.1f}')
print(f'{'Highest grade:':<20} {max_num:.1f}')
print(f'{'Sum of Grades:':<20} {sum:.1f}')
print(f'{'Average:':<20} {average:.2f}')
print('-------------------------------')

