# import random
# from models.enemy import *
# from models.rooms import *

# def seed_database():
#     Enemy.drop_table()
#     Enemy.create_table()

#     # Create seed data

#     enemies = []
#     rooms = [graveyard, rv_camp, town_square, drug_store, high_school, post_office, police_station]
#     for enemies in Enemy:
#         health = random.randint(1, 30)
#         location = random.choice(locations)
#         description = f"Zombie with health {health}"
#         zombie = Zombie(description = description, health = health, location = location)
#         zombies.append(zombie)


# seed_database()