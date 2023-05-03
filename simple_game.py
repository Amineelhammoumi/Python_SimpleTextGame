import random

def start_room():
    print("You are in a dark room. There is a door to your left and right. Which one do you choose?")

def treasure_room():
    print("You found a treasure chest! Congratulations, you won!")

def pit_room():
    print("You fell into a pit of spikes. Game over!")

def locked_door_room():
    print("You enter a room with a locked door. There is a key on the table. Do you take it?")
    choice = input("> ").lower()
    if choice == "yes":
        print("You took the key. Now, try unlocking the door.")
        return True  # Return True to indicate that the player has the key
    else:
        print("You didn't take the key. The door remains locked.")
        return False

def unlock_door_room(has_key):
    if has_key:
        print("You unlocked the door and found a hidden passage! Where does it lead?")
    else:
        print("The door is locked. You need a key to open it.")

def invalid_input():
    print("Invalid input. Please try again.")

def main_game_loop():
    current_room = start_room
    has_key = False
    game_over = False

    while not game_over:
        current_room()  # Call the current room function

        choice = input("> ").lower()

        if choice == "left" or choice == "right":
            if random.choice([True, False]):
                has_key = locked_door_room()
                current_room = lambda: unlock_door_room(has_key)
            else:
                pit_room()
                game_over = True
        else:
            current_room = invalid_input

if __name__ == "__main__":
    main_game_loop()
