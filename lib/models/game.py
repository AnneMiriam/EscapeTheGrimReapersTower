import random
from models.enemy import Enemy
from data.default_enemies import default_enemies
from NonPlayChar import *
from models.rooms import *

class Game:
    def __init__(self, player):
        self.player = player
        self.current_enemy = None
        
    def create_player(self):
        while True:
            print("Create a player.")
            player_username = input("Enter your name: ")
            try:
                # Initialize Player instance
                self.player = Player(player_username)
                break # Exit loop if successful
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
            hp=enemy_data['hp'],
            damage=enemy_data['damage'],
            name=enemy_data['name']
        )
        # Save the enemy to the database
        random_enemy.create_table()
        random_enemy.save()
        # Set the current_enemy to the randomly encountered enemy
        self.current_enemy = random_enemy