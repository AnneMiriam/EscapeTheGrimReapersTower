import random
from models.Enemy import Enemy
from data.default_enemies import default_enemies
from NonPlayChar import *
from models.rooms import *
from models.player import Player


class Game:
    def __init__(self, player):
        self.player = player
        self.current_enemy = None

    def create_player(self):
        while True:
            print("Create a player.")
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
