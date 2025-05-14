#Caelon Gooden
# 04/28/2025
# P5HW
#Create a game
import getpass
def create_wide_reciever():
    # Create a character with random attributes
    name = input("Enter your Wide Recievers's name: ")
    stamina = 100
    points = 100
    print(f"You have {points} points to spend on {name}'s attributes.")
    if points > 0:
        agility = int(input(f"How many points do you want to spend on {name}'s agility: "))

        while agility > points:
                print("You don't have enough points. Try again.")
                agility = int(input(f"How many points do you want to spend on {name}'s agility: "))
        points = points - agility
        print(f"You have {points} points left.")
        player_IQ = int(input(f"How many points do you want to spend on {name}'s offensive IQ: "))
                
        while player_IQ > points:        
                print("You don't have enough points. Try again.")
                player_IQ = int(input(f"How many points do you want to spend on {name}'s offensive IQ: "))
        points = points - player_IQ
        print(f"You have {points} points left.")
        speed = int(input(f"How many points do you want to spend on {name}'s speed: "))
        
        while speed > points:
                print("You don't have enough points. Try again.")
                speed = int(input(f"How many points do you want to spend on {name}'s speed: "))
        points = points - speed
        print(f"You have {points} points left.")
        press_ability = points
    print(f"You have {points} points remaining for {name}'s beat press ability.")
    character = {'Name': name, 'Stamina': stamina, 'Agility': agility, 'Offensive IQ': player_IQ, 'Speed': speed, 'Beat Press': press_ability}
    print(f"{name} has been created with the following attributes:")
    print(f"Stamina: {character['Stamina']}, Agility: {character['Agility']}, Offensive IQ: {character['Offensive IQ']}, Speed: {character['Speed']}, Beat Press: {character['Beat Press']}")
    return character
def create_defensive_back():
    # Create a character with random attributes
    name = input("Enter your Defensive Back's name: ")
    stamina = 100
    points = 100
    print(f"You have {points} points to spend on {name}'s attributes.")
    if points > 0:
        agility = int(input(f"How many points do you want to spend on {name}'s agility: "))
        while agility > points:
                print("You don't have enough points. Try again.")
                agility = int(input(f"How many points do you want to spend on {name}'s agility: "))
        points = points - agility
        print(f"You have {points} points left.")
        defensive_IQ = int(input(f"How many points do you want to spend on {name}'s defensive IQ: "))
        while defensive_IQ > points:
                print("You don't have enough points. Try again.")
                defensive_IQ = int(input(f"How many points do you want to spend on {name}'s defensive IQ: "))
        points = points - defensive_IQ
        print(f"You have {points} points left.")
        speed = int(input(f"How many points do you want to spend on {name}'s speed: "))
        while speed > points:
                print("You don't have enough points. Try again.")
                speed = int(input(f"How many points do you want to spend on {name}'s speed: "))
        points = points - speed
        print(f"You have {points} points left.")
        press = points
    print(f"You have {points} points remaining for {name}'s press ability.")
    character = {'Name': name, 'Stamina': stamina, 'Agility': agility, 'Defense IQ': defensive_IQ, 'Speed': speed, 'press': press}
    print(f"{name} has been created with the following attributes:")
    print(f"Stamina: {character['Stamina']}, Agility: {character['Agility']}, Defense IQ: {character['Defense IQ']}, Speed: {character['Speed']}, press: {character['press']}")
    return character
def display_characters(characters):
    # Display the character's attributes
    print('- - - - - - - - ALL CHARACTERS - - - - - - - - -')
    for character in characters:
     if 'Offensive IQ' in character:
         print(f"Name: {character['Name']}, Stamina: {character['Stamina']}, Agility: {character['Agility']}, Offensive IQ: {character['Offensive IQ']}, Beat Press: {character['Beat Press']}, Speed: {character['Speed']}")
     elif 'Defense IQ' in character:
         print(f"Name: {character['Name']}, Stamina: {character['Stamina']}, Agility: {character['Agility']}, Defense IQ: {character['Defense IQ']}, Press: {character['press']}, Speed: {character['Speed']}")

def skill_matchup(offense, defense):
      
      # Initialize x with a default value
    additional_yards = 0
    if offense['Agility'] > defense['Agility']:
        additional_yards = 5
        print(f"{offense['Name']} was able to break {defense['Name']}'s ankles and gained {additional_yards} additional yards on the play.")
        return additional_yards
    elif offense['Speed'] > defense['Speed']:
        additional_yards = 3
        print(f"{offense['Name']} was able to outrun {defense['Name']} and gained {additional_yards} additional yards on the play.")
        return additional_yards
    elif offense['Beat Press'] > defense['press']:
        additional_yards = 2
        print(f"{offense['Name']} was able to get loose off the line of scrimage and gained {additional_yards} additional yards on the play.")
        return additional_yards
    elif offense['Offensive IQ'] > defense['Defense IQ']:
        additional_yards = 4
        print(f"{offense['Name']} was able to outsmart {defense['Name']} and gained {additional_yards} additional yards on the play.")
        return additional_yards
    else:
        additional_yards = 0
    print(f"{defense['Name']} was able to slow {offense['Name']} down on this play! {offense['Name']} gained {additional_yards} yards.")
    return additional_yards

def pick_route(offense, defense):
    yards_gained = 0
    Offense = offense['Name']
    Defense = defense['Name']

    print(f"{Offense} pick your route!")
    print("1. Go Route")
    print("2. Slant Route")
    print("3. Post Route")
    print("4. Curl Route")
    offensive_choice = getpass.getpass("Choose an option: ")
    print(f"{Defense} guess the offense's play!")
    print("1. Go Route")
    print("2. Slant Route")
    print("3. Post Route")
    print("4. Curl Route")
    defensive_choice = getpass.getpass("Choose an option: ")
    if offensive_choice == defensive_choice:
        print(f"{Defense} was able to guess {Offense}'s route! No yards gained.")
        yards_gained = 0
        return yards_gained
    elif offensive_choice == '1' and defensive_choice == '2':
        print(f"{Offense} ran a Go Route and {Defense} guessed a Slant Route! {Offense} gained 20 yards.")
        yards_gained = 20
        return yards_gained 
    elif offensive_choice == '1' and defensive_choice == '3':
        print(f"{Offense} ran a Go Route and {Defense} guessed a Post Route! {Offense} gained 20 yards.")
        yards_gained = 20
        return yards_gained 
    elif offensive_choice == '1' and defensive_choice == '4':
        print(f"{Offense} ran a Go Route and {Defense} guessed a Curl Route! {Offense} gained 20 yards.")
        yards_gained = 20
        return yards_gained 
    elif offensive_choice == '2' and defensive_choice == '1':
        print(f"{Offense} ran a Slant Route and {Defense} guessed a Go Route! {Offense} gained 5 yards.")
        yards_gained = 5
        return yards_gained 
    elif offensive_choice == '2' and defensive_choice == '3':
        print(f"{Offense} ran a Slant Route and {Defense} guessed a Post Route! {Offense} gained 5 yards.")
        yards_gained = 5 
        return yards_gained 
    elif offensive_choice == '2' and defensive_choice == '4':
        print(f"{Offense} ran a Slant Route and {Defense} guessed a Curl Route! {Offense} gained 5 yards.")
        yards_gained = 5
        return yards_gained 
    elif offensive_choice == '3' and defensive_choice == '1':
        print(f"{Offense} ran a Post Route and {Defense} guessed a Go Route! {Offense} gained 15 yards.")
        yards_gained = 15
        return yards_gained 
    elif offensive_choice == '3' and defensive_choice == '2':
        print(f"{Offense} ran a Post Route and {Defense} guessed a Slant Route! {Offense} gained 15 yards.")
        yards_gained = 15
        return yards_gained 
    elif offensive_choice == '3' and defensive_choice == '4':
        print(f"{Offense} ran a Post Route and {Defense} guessed a Curl Route! {Offense} gained 15 yards.")
        yards_gained = 15
        return yards_gained 
    elif offensive_choice == '4' and defensive_choice == '1':
        print(f"{Offense} ran a Curl Route and {Defense} guessed a Go Route! {Offense} gained 10 yards.")
        yards_gained = 10
        return yards_gained 
    elif offensive_choice == '4' and defensive_choice == '2':
        print(f"{Offense} ran a Curl Route and {Defense} guessed a Slant Route! {Offense} gained 10 yards.")
        yards_gained = 10
        return yards_gained 
    else:
        print(f"{Offense} ran a Curl Route and {Defense} guessed a Post Route! {Offense} gained 10 yards.")
        yards_gained = 10
        return yards_gained 
def main():
    play_again = "play again" or "Play Again"
    while play_again == "play again":
        print("Welcome to the Football Game!")
        print("You will create two characters: a Wide Receiver and a Defensive Back.")
        
        # Create characters
        wide_reciever = create_wide_reciever()
        defensive_back = create_defensive_back()

        # Display all characters
        characters = [wide_reciever, defensive_back]
        display_characters(characters)

        input("When you are ready to start the game, press Enter.")
        total_yards = 0
        offensive_stamina = wide_reciever['Stamina']
        defensive_stamina = defensive_back['Stamina']
        num_of_downs = 4
        yards_gained = 0
        matchup_result = 0

          # Ensure yards_gained is initialized
        while num_of_downs > 0 and offensive_stamina > 0 and defensive_stamina > 0 and total_yards < 100:
            print(f"Plays remaining: {num_of_downs}")
            print("Pick a play...")
            print(f"{wide_reciever['Name']}'s stamina: {offensive_stamina}")
            print(f"{defensive_back['Name']}'s stamina: {defensive_stamina}")
            yards_gained = pick_route(wide_reciever, defensive_back) 
            if yards_gained > 0:
                matchup_result = skill_matchup(wide_reciever, defensive_back)
                if matchup_result == 0:
                    print(f"{wide_reciever['Name']} successfully completed the route, but got no additional yards!")
                    total_yards = yards_gained
                    defensive_back['Stamina'] = max(0, defensive_back['Stamina'] - 5)
                    defensive_stamina = defensive_back['Stamina']
                    print(f" {defensive_back['Name']} was unable to stop the wide receiver, but was able to recover due to his abilities. He lost less stamina.")
                    print(f"{wide_reciever['Name']} now has total yards: {total_yards}")
                    num_of_downs = 4
                else:
                    total_yards += yards_gained + matchup_result
                    defensive_back['Stamina'] = max(0, defensive_back['Stamina'] - 10)
                    defensive_stamina = defensive_back['Stamina']
                    print(f"Since {defensive_back['Name']} was unable to stop {wide_reciever['Name']}, he lost stamina.")
                    print(f"{wide_reciever['Name']} now has total yards: {total_yards}")
                    num_of_downs = 4
            else:
                total_yards += yards_gained
                wide_reciever['Stamina'] = max(0, wide_reciever['Stamina'] - 20)
                offensive_stamina = wide_reciever['Stamina']
                print(f"Since {wide_reciever['Name']} was stopped on this play, he also lost stamina.")
                print(f"{wide_reciever['Name']} now has total yards: {total_yards}")
                num_of_downs = num_of_downs - 1
        if num_of_downs <= 0:
            print(f"Game Over! {defensive_back['Name']} was able to get a turnover on downs. {defensive_back['Name']} has won the game!")
            run_again = input("Would you like to play again or end the game? ")
            if run_again == 'play again':
                main()
            else:
                print("Thanks for playing!")
                return
        elif offensive_stamina <= 0 or defensive_stamina <= 0:
            print("One of the players has run out of stamina. The game is over.")
            run_again = input("Would you like to play again or end the game? ")
            if run_again == 'play again':
                main()
            else:
                print("Thanks for playing!")
                return
        elif total_yards >= 100:
            print(f"Touchdown! {wide_reciever['Name']} won the game!")
            run_again = input("Would you like to play again or end the game? ")
            if run_again == 'play again':
                main()
            else:
                print("Thanks for playing!")
                return    
if __name__ == "__main__":
        main()