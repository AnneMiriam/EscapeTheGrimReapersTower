import random
from models.items import *
from models.enemy import Enemy
from data.default_enemies import default_enemies
from models.items import *
from models.NonPlayChar import *
from models.rooms import *
from models.player import Player
from helpers import output_slow, output_slower
from models.items import StaleBread, MoldyApple, MysteriousLiquid, Rope, QuestionableLiquid


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_enemy = None
       

    #  trading code
    def trade(self, consumer, seller):
        room = TradingGhost()
        seller = room.trader

        while True:
            for i, item in enumerate(seller.inventory, 1):
                print("{}. {}".format(i, item))

            user_input = input("Select your item or press q to exit >> ")

            if user_input == "q":
                Game.return_staircase(self)
                break

            try:
                choice = int(user_input)
                if choice < 1 or choice > len(seller.inventory):
                    raise ValueError("Unacceptable selection! Choose more wisely")

                initial_hp = consumer.hp
                exchange = seller.inventory[choice - 1]
                self.transaction(seller, consumer, exchange)
                hp_change = exchange.healing_value
                consumer.hp = initial_hp + hp_change

                hp_change_str = (
                    f"({hp_change} HP)" if hp_change < 0 else f"(+{hp_change} HP)"
                )

                print(
                    f"Trade sealed in ethereal terms. Your updated HP: {consumer.hp} ({hp_change_str}))"
                )

            except ValueError as e:
                print(e)
                continue

    def transaction(self, seller, consumer, item):
        if isinstance(consumer, Player) and hasattr(item, "healing_value"):
            if item.healing_value > consumer.hp:
                print(
                    "Oh no dearie, that simply won't do. It seems you do not have enough vitality to share! But do feel free to come back when you're feeling stronger."
                )
                return
            seller.inventory.remove(item)
            consumer.inventory.append(item)

            if item.healing_value < 0:
                print("Trade sealed in ethereal terms.")
                print(f"Your updated HP: {consumer.hp} ({item.healing_value} HP)")
            else:
                consumer.hp += item.healing_value
                print("Trade sealed in ethereal terms.")
                print(f"Your updated HP: {consumer.hp} (+{item.healing_value})")

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

    def create_enemy(self):
        while True:
            print("What kind of enemy")
            enemy_name = input("Enter it's name: ")
            # enemy_damage = input("How much damage can your enemy cause: " )
            try:
                # Initialize enemy instance
                self.enemy = Enemy(enemy_name)
                break  # Exit loop if successful
            except ValueError as e:
                print(e)
                continue
        # Create table and save enemy object to db
        self.enemy.create_table()
        self.enemy.save()

    # def random_encounter(self):
    #     enemy_data = random.choice(default_enemies)
    #     # Create an Enemy instance with random attributes
    #     if "hp" in enemy_data and "damage" in enemy_data and "name" in enemy_data:
    #         random_enemy = Enemy(
    #             hp=enemy_data["hp"],
    #             damage=enemy_data["damage"],
    #             name=enemy_data["name"],
    #         )
    #         # Save the enemy to the database
    #         random_enemy.create_table()
    #         random_enemy.save()
    #         # Set the current_enemy to the randomly encountered enemy
    #         self.current_enemy = random_enemy
    #     else:
    #         print("Invalid enemy data. Missing required attributes.")
            
    # Battle Code
    def random_encounter(self):
        enemy_types = [
            GrimReaper, BlackCat, Poltergeist, BlackWidow,
                       Enemy.find_by_id(-1)]
        random_enemy_type = random.choice(enemy_types)
        # random_enemy_type = EnemyAndFriends(enemy_types)
        random_enemy = random_enemy_type()
        self.current_enemy = random_enemy

    def battle(self):
        if not self.player or not self.current_enemy:
            print("Must be alive to battle")
            return
        # print(f"A {self.current_enemy} appeared!")
        while self.player.hp > 0 and self.current_enemy.hp > 0:
            print(f"{self.player.name}'s HP: {self.player.hp}")
            print(f"{self.current_enemy.name}' HP: {self.current_enemy.hp}")

            player_choice = input("(a)ttack or (r)un >> ")
            if player_choice == "a":
                self.attack(self.player, self.current_enemy)
            if player_choice == "r":
                print()
                output_slow(
                    "You flee back to the attic room. It may not be home, but it's the only room you've been safe in so far."
                )
                Game.return_attic_room(self)
            else:
                print("Invalid choice. You must battle or flee...")

            if self.current_enemy.hp <= 0:
                print(f"{self.current_enemy.dead_text} \nYou defeated the {self.current_enemy.name}!")
                break

            self.attack(self.current_enemy, self.player)
            if self.player.hp <= 0:
                print()
                output_slow("You have become another soul within the tower")
                output_slower("GAME OVER")
                exit()

    # attack code
    def attack(self, attacker, target):
        attacker_damage = attacker.damage
        print(f"{attacker.name} attacks {target.name} for {attacker_damage} damage!")
        target.hp -= attacker_damage

            
    #START GAME and room navigation
    def start_game(self):
        room = AtticRoom()
        print()
        output_slow(room.intro_text())
        print()
        print("1. Go to window \n2. Go to door \n3. Check inventory")
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.go_attic_window(self)
        if choice == "2":
            Game.go_staircase(self)
        if choice == "3":
            self.player.print_inventory()
            Game.return_attic_room(self)

    def go_attic_window(self):
        room = AtticRoomWindow()
        print()
        output_slow(room.intro_text())
        print()
        print(
            "1. Go back to the relative safety of the attic room \n2. Take your chances and leap \n3. Check inventory"
        )
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.return_attic_room(self)
        if choice == "2":
            print()
            output_slow(
                "Almost as soon as your feet leave the railing, you know you made a grave mistake. As you fall you reach out, trying to grasp for the railing of the balcony below you, but the rain prevents you from finding purchase. Your eyes go wide with horror as time slows. You hear a low, rumbling laugh like the sound of hundreds of clacking bones as the lights of the tower rooms grow farther away. No longer able to bear the sight of your own iminent death - your failure - you close your eyes and wait for the pain."
            )
            output_slower("GAME OVER")
            exit()
        if choice == "3":
            self.player.print_inventory()
            Game.go_attic_window

    def return_attic_room(self):
        room = AtticRoom()
        print()
        output_slow(room.return_text())
        print()
        print("1. Go to window \n2. Go to door \n3. Check inventory")
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.go_attic_window(self)
        if choice == "2":
            Game.go_staircase(self)
        if choice == "3":
            self.player.print_inventory()
            Game.return_attic_room

    def go_staircase(self):
        room = StairCase()
        print()
        output_slow(room.intro_text())
        print()
        print(
            "1. Go to the fourth floor door \n2. Go to the third floor door \n3. Go to the second floor door \n4. Go to the first floor door \n5. Go to the entryway \n6. Return to attic room \n7. Meet the ghost \n8. Check inventory"
        )

        choice = input("What will you do? >> ")

        if choice == "1":
            Game.go_fourth_floor(self)
        if choice == "2":
            Game.go_third_floor(self)
        if choice == "3":
            Game.go_second_floor(self)
        if choice == "4":
            Game.go_first_floor(self)
        if choice == "5":
            Game.go_entryway(self)
        if choice == "6":
            Game.return_attic_room(self)
        if choice == "7":
            Game.go_trading(self)
        if choice == "8":
            self.player.print_inventory()
            Game.return_staircase(self)

    def return_staircase(self):
        room = StairCase()
        # encounter code
        encounter_chance = random.random()
        print(f"Encounter chance: {encounter_chance}")
        if encounter_chance < 0.2:
            self.random_encounter()

        if self.current_enemy:
            print(f"{self.current_enemy.alive_text}")
            self.battle()
        print()
        output_slow(room.return_text())
        print()
        print(
            "1. Go to the fourth floor door \n2. Go to the third floor door \n3. Go to the second floor door \n4. Go to the first floor door \n5. Go to the entryway \n6. Return to attic room \n7. Check inventory"
        )
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.go_fourth_floor(self)
        if choice == "2":
            Game.go_third_floor(self)
        if choice == "3":
            Game.go_second_floor(self)
        if choice == "4":
            Game.go_first_floor(self)
        if choice == "5":
            Game.go_entryway(self)
        if choice == "6":
            Game.return_attic_room(self)
        if choice == "7":
            self.player.print_inventory()
            Game.return_staircase(self)

    def go_fourth_floor(self):
        room = FourthFloorRoom()
        # encounter code
        encounter_chance = random.random()
        print(f"Encounter chance: {encounter_chance}")
        if encounter_chance < 0.9:
            self.random_encounter()

        if self.current_enemy:
            print(f"{self.current_enemy.alive_text}")
            self.battle()
        print()
        output_slow(room.intro_text())
        print()
        print("1. Return to the staircase \n2.Check inventory")
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.return_staircase(self)
        if choice == "2":
            self.player.print_inventory()
            Game.go_fourth_floor(self)

    def go_third_floor(self):
        room = ThirdFloorRoom()
        print()
        output_slow(room.intro_text())
        print()
        print("1. Go to the window \n2. You're exhausted: Take a nap on the bed \n3. Return to staircase \n4. Check inventory")
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.go_third_floor_window(self)
        if choice == "2":
            # encounter code
            encounter_chance = random.random()
            print(f"Encounter chance: {encounter_chance}")
            if encounter_chance < 0.3:
                self.random_encounter()

            if self.current_enemy:
                print(f"{self.current_enemy.alive_text}")
                self.battle()
            print()
            output_slow("What are you doing napping at a time like this!")            
            Game.go_third_floor(self)
        if choice == "3":
            Game.return_staircase(self)
        if choice == "4":
            self.player.print_inventory()
            Game.go_third_floor(self)

    def go_trading(self):
        room = TradingGhost()
        print()
        output_slow(room.intro_text())
        print("1. Trade \n2. Return to staircase")
        choice = input("Would you like to test your fate? >> ")
        if choice == "1":
            print()
            print("Behold, these are the offerings for trade from beyond the veil:")
            self.trade(self.player, room.trader)
        if choice == "2":
            Game.return_staircase(self)

    def go_third_floor_window(self):
        room = ThirdFloorWindow()
        print()
        output_slow(room.intro_text())
        print()
        print(
            "1. Go back to the relative safety of the room \n2. Take your chances and leap \n3. Check inventory"
        )
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.go_third_floor(self)
        if choice == "2":
            print()
            output_slow(
                "Almost as soon as your feet leave the railing, you know you made a grave mistake. As you fall you reach out, trying to grasp for the railing of the balcony below you, but the rain prevents you from finding purchase. Your eyes go wide with horror as time slows. You hear a low, rumbling laugh like the sound of hundreds of clacking bones as the lights of the tower rooms grow farther away. No longer able to bear the sight of your own iminent death - your failure - you close your eyes and wait for the pain."
            )
            output_slower("GAME OVER")
        if choice == "3":
            self.player.print_inventory()
            Game.go_third_floor_window(self)

    def go_second_floor(self):
        room = SecondFloorRoom()
        print()
        output_slow(room.intro_text())
        print()
        print("1. Investigate desk \n2. Return to staircase \n3. Check Inventory")
        choice = input("Whhat will you do? >> ")
        if choice == "1":
            print()
            output_slow(
                "You open the drawer. Not much stands out to you at first - a couple of papers, some old letters maybe - but as you sift through the contents you find a large iron skeleton key. This may come in handy."
            )
            self.player.add_to_inventory(Key())
            Game.go_second_floor(self)
        if choice == "2":
            Game.return_staircase(self)
        if choice == "3":
            self.player.print_inventory()
            Game.go_second_floor(self)
            
    def go_first_floor_window(self):
        room = FirstFloorWindow()
        print()
        output_slow(room.intro_text())
        print()
        print(
            "1. Go back to the relative safety of the room \n2. Take your chances and leap"
        )
        choice = input("Where will you go? >> ")
        if choice == "1":
            Game.go_first_floor(self)
        if choice == "2":
            random_fate = random.random()
            print(f"Random fate: {random_fate}")
            if random_fate < 0.5:
                print()
                output_slow("You step onto the railing and almost loose your footing. 'That was close', you thought. You can vaguely see the ground below, it doesn't seem that far. You hear a low, rumbling laugh, like the tower itself is laughing. You know it is now or never! You take a deep breath and jump. \n \n Your feet hit the ground, a stinging pain rushes through them, but you are alive. And FREE!")
                output_slower("YOU HAVE ESCAPED DEATH! YOU WIN!")
                exit()
            else:
                print()
                output_slow(
                    "As you step onto the railing you loose your footing on the slippery metal, you know you made a grave mistake. You can see the ground raising towards you. Your eyes go wide with horror as time slows. You hear a low, rumbling laugh - you close your eyes and wait for the pain."
                )
                output_slower("GAME OVER")

    def go_first_floor(self):
        room = FirstFloorRoom()
        encounter_chance = round(random.random(), 1)
        print(f"Encounter chance: {encounter_chance}")
        if encounter_chance < 0.5:
            self.random_encounter()

        if self.current_enemy:
            print(f"{self.current_enemy.alive_text}")
            self.battle()
        print()
        output_slow(room.intro_text())
        print()
        print("1.Go to the window \n2. Return to staircase \n3. Check inventory")
        choice = input("What will you do? >> ")
        if choice == "1":
            Game.go_first_floor_window(self)
        if choice == "2":
            Game.return_staircase(self)
        if choice == "3":
            self.player.print_inventory()
            Game.go_first_floor(self)

    def go_entryway(self):
        room = EntryWay()
        print()
        output_slow(room.intro_text())
        print()
        print(
            "1.Try your luck with the front door \n2. Return to staircase \n3. Check inventory"
        )
        choice = input("What will you do? >> ")
        if choice == "1":
            if any(isinstance(item, Key) for item in self.player.inventory):
                print()
                output_slow("As you place your hand on the handle")
                output_slower("YOU HAVE ESCAPED DEATH")
                exit()
            else:
                print()
                output_slow(
                    "You pull at the handles of the double doors as hard as you can, but they won't budge an inch. You notice a large keyhole on one of the doors. Maybe the key is around here somewhere?"
                )
                Game.return_entryway(self)
        if choice == "2":
            Game.return_staircase(self)
        if choice == "3":
            self.player.print_inventory()
            Game.return_entryway(self)

    def return_entryway(self):
        room = EntryWay()
        print()
        output_slow(room.return_text())
        print()
        print(
            "1.Try your luck with the front door \n2. Return to staircase \n3. Check inventory"
        )
        choice = input("What will you do? >> ")
        if choice == "1":
            if any(isinstance(item, Key) for item in self.player.inventory):
                print()
                output_slow("You get out and win!")
                output_slower("YOU HAVE ESCAPED DEATH")
                exit()
            else:
                print()
                output_slow(
                    "You pull at the handles of the double doors as hard as you can, but they won't budge an inch. You notice a large keyhole on one of the doors. Maybe the key is around here somewhere?"
                )
                Game.return_entryway(self)
        if choice == "2":
            Game.return_staircase(self)
        if choice == "3":
            self.player.print_inventory()
            Game.return_entryway(self)

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

    
