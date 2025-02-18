#Juan Gonzalez

# Dictionary for rooms and items
systems = {
    'System Alliance Home': {'North': 'Leviathan System', 'East': 'Asarian System', 'South': 'Krogan System', 'West': 'Turian System', 'Item': None},
    'Leviathan System': {'South': 'System Alliance Home', 'East': 'Omega System', 'Item': 'Leviathan Orb'},
    'Omega System': {'West': 'Leviathan System', 'Item': None}, #Villian Room
    'Asarian System': {'West': 'System Alliance Home', 'North': 'Quarian System', 'Item': 'Prothean Beacon'},
    'Quarian System': {'South': 'Asarian System', 'Item': 'Kinetic Amplifier'},
    'Turian System': {'East': 'System Alliance Home', 'Item': 'Power Core'},
    'Krogan System': {'North': 'System Alliance Home', 'East': 'Batarian System', 'Item': 'Threser Maw Ore'},
    'Batarian System': {'West': 'Krogan System', 'Item': 'Element Zero'}
}

# Prompt for game initializing
print('''
=====================
|      Destroy      |
|        the        |
|       Reaper      |
=====================
''')

# Prompt for player name
player_name = input('What is your name?').strip().capitalize()

# Prompt welcome and mission statement
print(f'''
Welcome to the System Alliance Navy {player_name}!

You will be going on a mission in the System Alliance's most advanced ship, the Normandy SSV.

Your mission will be to collect six items throughout multiple star systems to be able to take down the galaxy's most formidable foe, the Reaper.

Intelligence says the Reaper was last spotted in the Omega System. Be wary of running into the Reaper before collecting all of the items.

So remember to check your inventory to keep track of your items!
''')

# Command to start or quit the game at menu
while True:
    player_start = input('\nEnter \'start\' to begin your mission or \'quit\' to exit.').strip().capitalize()
    if player_start in {'Start', 'Quit'}:
        break
    else:
        print('\nInvalid command. Please enter \'start\' or \'quit\'.')

# Set starting position and current items
current_system = 'System Alliance Home'
collected_items = []
all_items_collected = False  # Flag to track if all items have been collected

# Set function for player movement
def move_player(direction, current_location):
    if direction in systems[current_location]:
        return systems[current_location][direction]
    else:
        print('\nYou can\'t go that way. Try a different direction.')
        return current_location  # Return value to stay in the same location if movement is not possible

# Set function to collect items
def collect_item(current_location, collected_items):
    item = systems[current_location].get('Item')
    if item and item not in collected_items:
        while True:
            collect = input(f'\nYou have found {item}. Do you want to collect it? (yes/no)').strip().lower()
            if collect in {'yes', 'no'}:
                break
            else:
                print('\nInvalid input. Please enter \'yes\' or \'no\'.')
        if collect == 'yes':
            collected_items.append(item)
            print(f'You have collected: {item}')
    return collected_items

# Main game loop
if player_start == 'Start':
    game_over = False

    print(f'\nYou are in the {current_system}.')
    while not game_over:
        player_input = input('\nEnter a command (North, East, South, West, Location) or \'quit\' to end the mission: ').strip().capitalize()

        if player_input == 'Quit': #If player quits during the game
            print(f'\nReturn home {player_name}. We will regroup and fight the Reaper another day!')
            game_over = True
        elif player_input in {'North', 'East', 'South', 'West'}: #Player direction input and movement
            new_system = move_player(player_input, current_system) #Update player location
            if new_system != current_system: #Update once player moves from current location
                print(f'\nYou are in the {new_system}.')
                print(f'Current items collected: {collected_items}')
                current_system = new_system
                collected_items = collect_item(current_system, collected_items)
                if current_system == 'Omega System' and len(collected_items) < 6:  # If player encounters Reaper without all items
                    print('\nYou have encountered the Reaper without collecting all items. The Normandy SSV has been destroyed! Mission Failed.')
                    game_over = True
                elif len(collected_items) == 6 and not all_items_collected:  # Prompt once player collects all items
                    all_items_collected = True #Flag turns True once all items are collected
                    print('\nYou have collected all items and are ready to defeat the Reaper!')
                    continue  # Skip the rest of the loop to avoid printing prompt constantly
                elif current_system == 'Omega System' and all_items_collected:  # If player encounters Reaper with all items
                    print('\nCongratulations, you have defeated the Reaper and brought peace to the galaxy!')
                    game_over = True

        elif player_input == 'Location':
            print(f'\nYou are currently in the {current_system}.')  #Display current location
        else:
            print('\nInvalid command. Please enter a valid input.')

# Exit prompt if player exits at menu
if player_start == 'Quit':
    print('Goodbye!')

# Prompt to hit enter to exit after winning
if game_over and all_items_collected:
    input('\nPress Enter to exit the game.')
