# lib/helpers.py
import time
from models.enemy import Enemy
from models.NonPlayChar import NonPlayableCharacter
from models.player import Player
from models.rooms import MapRoom


def display_intro():
    output_slow("It's the cold that wakes you.")
    print()
    output_slow(
        "It's a cold that doesn't just raise the hairs on your arms and make your fingers feel stiff, but rather sinks deep beneath your skin, prickling at the marrow in your bones. You scramble to your feet, slipping slightly on the slick stone floor."
    )
    print()
    output_slow(
        "The room you find yourself in is bare, its rough hewn stone walls illuminated only by a lantern hanging from the arched cieling."
    )

    output_slow(
        "Ahead of you stands a plain wooden door with a tarnished brass handle."
    )

    output_slow(
        "Behind you a window rattles, battered by the force of the shrieking wind."
    )
    print()
    output_slow(
        "Panic fills your mind like a dull roar as you begin to grasp the danger you are in, until you are left with only one coherent thought: you have to get out."
    )
    print()
    print()


def helper_1():
    print("Performing useful function#1.")


def output_slow(output):
    for char in output:
        print(char, end="", flush=True)

        time.sleep(0.001)


    print()


# outputs cli text slower
def output_slower(output):
    for char in output:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print()


def exit_program():
    print("Goodbye!")
    exit()
