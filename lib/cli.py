# lib/cli.py

from helpers import (
    display_intro,
    exit_program,
    helper_1
)


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
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("What do you want to do?")
    print("0. Exit the program")
    print("1. Take a breath - remember who you are")


if __name__ == "__main__":
    main()
