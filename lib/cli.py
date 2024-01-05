# lib/cli.py

from helpers import display_intro, exit_program, output_slower
from models.game import Game
from models.player import Player
from models.enemy import Enemy


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
            # create an enemy in the Enemy class
            game = Game(None, None)
            game.create_enemy()
            new_menu()
            
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
    print("2. Look up created enemies")
    print("3. Delete created enemies")
    print("4. Create another enemy")
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        print("-" * 50)
        # Start new game session. Initialize game with player and pass onto Game.
        game = Game(None, None)
        game.create_player()
        game.start_game()
    elif choice == "2":
        # Get all the enemy's names
        enemies = Enemy.get_all()
        for enemy in enemies:
            print(enemy.name)
        new_menu()
    elif choice == "3":
        # get the enemies by name and delete them
        value = input("What enemy do you seek? >>")
        nemesis = Enemy.find_by_name(value)
        if nemesis:
            nemesis.delete()
            print()
            print("You have eliminated an enemy!")
        else:
            print("This enemy does not exist! Look for another or play the game.")
        new_menu()
    elif choice == "4":
        # create an enemy in the Enemy class
        game = Game(None, None)
        game.create_enemy()
        new_menu()


if __name__ == "__main__":
    main()
