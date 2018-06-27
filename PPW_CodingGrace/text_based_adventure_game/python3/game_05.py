# Now we have a premise. We are in a room and we have two door to choose from.
# We are still in the red room, and we updated this program with the 
# function you_died with a given reason.
#
# Run this code a few times and see what happens with different choices.
# It's good to test all options and see if that's what you expected.

##### ACTIONS #####
def you_died(why):
    '''
    In: Passing in the string showing player how they dies 

    Result: 
    Prints reason why they player died. 
    Programme exits without error.
    '''
    # You expect a reason why the player died. It's a string.
    print(f"{why}. Good job!")

    # This exits the program entirely.
    exit(0)

### END ACTIONS ###

##### ROOMS #####
def blue_door_room():
    '''
    This is a blue door room.

    Nothing happens here, let's do one room at the time. :-)
    '''
    print("The door knob jiggles but nothing happens.")
    return

def red_door_room():
    '''
    The red door rooom contains a red dragon.
    
    If a player types "flee" as an answer, player returns to the room with two doors,
    otherwise the player dies.
    '''
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")
### END ROOMS ###

def start_adventure():
    '''
    This function starts the adventure by allowing two options for 
    players to choose from: red or blue door

    Chosen option will print out the door chosen.
    '''
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

def main():
    '''
    Gets the players name, print it out and starts the adventure.
    '''
    player_name =  input("What's your name? >")
    print(f"Your name is {player_name.upper()}")

    start_adventure()

if __name__ == '__main__':
    main()