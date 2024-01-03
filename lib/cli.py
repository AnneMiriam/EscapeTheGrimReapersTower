# lib/cli.py

from helpers import (
    exit_program,
    output_slower
)
from models.game import Game

def main():

    # Main game loop
    
    output_slower("\nWelcome to The Grim Reaper's Tower Escape game:\n")
    output_slower("\nYou have woken up in attic of a 5 floor tower. \n")
    output_slower("\nYou must escape from the tower, either out the front door on the ground level or by repelling down from a window. \n")
    output_slower("\nThere are items that you must find to help you escape, such as the key to the front door/front gate or rope to help you out the window.\n")
    output_slower("\nBeware the Grim Reaper is hiding in the tower. If you meet him you will loose a random amount of HP. And he isn't alone. \n")
    output_slower("\nThere are, also, potential friends in the tower that may have something you need. \n")
    output_slower("\nAfter you press enter, your character will be taken directly into the game where you start with HP of 50.\n")
        
    
# def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("-" * 50)
                # Start new game session. Initialize game with player and pass onto Game.
            game = Game(None, None)
            game.create_player()
            game.start_game()
            print("Enter your choice >>")
            print("-" * 50)
            continue
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Start Game")


if __name__ == "__main__":
    main()
