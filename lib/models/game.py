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
        output_slow(room.intro_text())
        print("1. Window \n2. Door")
        choice = input("Where will you go? > ")
        if choice == "1":
            output_slow(
                "The window shakes violently as you approach, the wind outside whipping up into a frenzy. The balcony is soaking wet from the rain, and as you peer over the edge you realize you cannot see the ground. You can, however, see another small balcony a few floors below you."
            )
            # print("1. Return to the relative safety of the room \n2. Take your chances and leap")
            # if choice == "1":
            #     output_slow("You return to the attic room.")
            #     print("1. Door")
            #     if choice =="1":
            #         pass
            # if choice =="2":
            #     output_slow("You ded")
            #     output_slower("GAME OVER")
            #     exit()
        if choice == "2":
            pass

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
