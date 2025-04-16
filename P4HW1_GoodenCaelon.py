#Caelon Gooden
# Date: 04/15/25
#P4HW1
#Collect scores from user, incorporate scores into a loop and display results
#Get number of scores from user
num_score=int(input("How many scores do you want to enter? "))
print("")
#Create empty list for scores
score_list = []
#Loop to get scores from user and check if scores are valid
#If invalid, prompt user to enter score again
for number in range(1, num_score + 1):
    score = float(input(f"Enter score #{number}: "))
    while score < 0 or score > 100:
        print("")
        print("INVALID Score entered!!!!")
        print("Score must be between 0 and 100")
        score = float(input(f"Enter score #{number} again: "))
        #add scores to list
    else:
        round(score, 1)
        score_list.append(score)
        
#Remove lowest score and calculate average
low_score = min(score_list)
score_list.remove(low_score)
average = sum(score_list) / len(score_list)
#Display lowest score, modified list, average, and letter grade
print("")
print("")
print('------------Results------------')
print(f'{"Lowest score  : "} {low_score:.1f}')
print(f'{"Modified List : "} {score_list}')
print(f'{"Scores Average: "} {average:.2f}')
print(f'{"Grade         : "}', end=" ")
# Determine the letter grade based on the average
if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
else:
    print("F")
print('-------------------------------')
#End of program


     