# lib/helpers.py
import time
from models.enemy import Enemy
from models.NonPlayChar import NonPlayableCharacter
from models.player import Player
from models.rooms import MapRoom


def helper_1():
    print("Performing useful function#1.")

# outputs cli text slower
def output_slower(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()


def exit_program():
    print("Goodbye!")
    exit()
