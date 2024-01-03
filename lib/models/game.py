import random
from models.Enemy import Enemy
from data.default_enemies import default_enemies
from models.NonPlayChar import *
from models.rooms import *
from models.player import Player
from helpers import output_slow, output_slower


class Game:
    def __init__(self, player):
        self.player = player
        self.current_enemy = None

    def create_player(self):
        while True:
            print("Create a player.")
            print("Who are you?")

            player_name = input("Enter your name: ")
            try:
                # Initialize Player instance
                self.player = Player(player_name)
                break  # Exit loop if successful
            except ValueError as e:
                print(e)
                continue
        # Create table and save player object to db
        self.player.create_table()
        self.player.save()

    def random_encounter(self):
        enemy_data = random.choice(default_enemies)
        # Create an Enemy instance with random attributes
        random_enemy = Enemy(
            hp=enemy_data["hp"], damage=enemy_data["damage"], name=enemy_data["name"]
        )
        # Save the enemy to the database
        random_enemy.create_table()
        random_enemy.save()
        # Set the current_enemy to the randomly encountered enemy
        self.current_enemy = random_enemy

    def start_game(self):
        room = AtticRoom()
        print()
        output_slow(room.intro_text())
        print()
        print("1. Window \n2. Door")
        choice = input("Where will you go? > ")
        if choice == "1":
            Game.go_attic_window(self)
        if choice == "2":
            Game.go_staircase(self)

    def go_attic_window(self):
        room = AtticRoomWindow()
        print()
        output_slow(room.intro_text())
        print()
        print(
            "1. Go back to the relative safety of the attic room \n2. Take your chances and leap"
        )
        choice = input("Where will you go? > ")
        if choice == "1":
            Game.return_attic_room(self)
        if choice == "2":
            print("GAME OVER")
            exit()

    def return_attic_room(self):
        room = AtticRoom()
        print()
        output_slow(room.return_text())
        print()
        print("1. Window \n2. Door")
        choice = input("Where will you go? > ")
        if choice == "1":
            Game.go_attic_window(self)
        if choice == "2":
            Game.go_staircase(self)

    def go_staircase(self):
        room = StairCase()
        print()
        output_slow(room.intro_text())
        print()
        print(
            "1. Fourth floor door \n2. Third floor door \n3. Second floor door \n4. First floor door \n5. Entryway \n6. Return to attic room"
        )
        choice = input("Where will you go? > ")
        if choice == "1":
            pass
        if choice == "2":
            pass
        if choice == "3":
            pass
        if choice == "4":
            pass
        if choice == "5":
            pass
        if choice == "6":
            Game.return_attic_room(self)

    # def random_encounter(self):
    #     enemy_data = random.choice(default_enemies)
    #     # Create an Enemy instance with random attributes
    #     random_enemy = Enemy(
    #         hp=enemy_data['hp'],
    #         damage=enemy_data['damage'],
    #         name=enemy_data['name']
    #     )
    #     # Save the enemy to the database
    #     random_enemy.create_table()
    #     random_enemy.save()
    #     # Set the current_enemy to the randomly encountered enemy
    #     self.current_enemy = random_enemy


# Battle Code

# def battle(self):
#     if not self.player or not self.current_enemy:
#         print("Must be alive to battle")
#         return
#     print(f"A {self.current_enemy} appeared!")

#     while self.player.hp > 0 and self.current_enemy.hp > 0:
#         print(f"{self.player.name}'s HP: {self.player.hp}")
#         print(f"{self.current_enemy.name}' HP: {self.current_enemy.hp}")

#     player_choice = input("Press 'a' to attack:")
#     if player_choice in ["a"]:
#         self.attack(self.player, self.current_enemy)
#     else:
#         print("Invalid choice. You must battle")

#     if self.current_enemy.hp <= 0:
#         print(f"You defeated {self.current_enemy.name}!")

#     self.attack(self.current_enemy, self.player)
#     if self.player.hp <= 0:
#         print("You have become another soul within the tower")

# def attack(self, attacker, target):
#     damage = attacker.damage
#     print(f"{attacker.name} attacks {target.name} for {damage} damage!")
#     target.hp -= damage


# encounter code

# encounter_chance = random.random()
# if encounter_chance < 0.9:
#     print(f"A {self.current_enemy} appeared!")
#     self.random_encounter()

#     if self.current_enemy:
#         self.battle()
