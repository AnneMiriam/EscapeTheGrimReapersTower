# lib/cli.py

from helpers import display_intro, exit_program, output_slower
from models.game import Game


def main():
    while True:
        print()
        print()
        print("ESCAPE THE GRIM REAPER'S TOWER")
        print()
        print()
        display_intro()
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
            # print("Enter your choice >>")
            # print("-" * 50)
        elif choice == "2":
            game = Game(None, None)
            game.create_enemy()
            new_menu()
            choice = input("> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                print("-" * 50)
                # Start new game session. Initialize game with player and pass onto Game.
                game = Game(None, None)
                game.create_player()
                game.start_game()
            break
        else:
            print("Invalid choice")


def menu():
    print("What do you want to do?")
    print("0. Exit the program")
    print("1. Take a breath - remember who you are")
    print("2. Extra Challenge - create an enemy")


def new_menu():
    print("What do you want to do?")
    print("0. Exit the program")
    print("1. Take a breath - remember who you are")


if __name__ == "__main__":
    main()
