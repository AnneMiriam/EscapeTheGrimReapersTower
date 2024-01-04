import re
from lib.models.rooms import *
from models.items import *
from models.__init__ import CURSOR, CONN


class Player:
    ALL = {}

    def __init__(self, name, id=None):
        self.id = id
        self.hp = 50
        self.name = name
        self.inventory = []
        self.damage = 5
        self.victory = False
        self.location = AtticRoom()

    def __repr__(self):
        return f"Current unfortunate soul: {self.name}" + f"Life remaining: {self.hp}"

    def print_inventory(self):
        if self.inventory:
            print()
            print("Inventory:")
            for item in self.inventory:
                print("*" + str(item))
        else:
            print()
            print("Your pockets are empty, save for a bit of lint and some old crumbs.")
            

    def add_to_inventory(self, item):
        self.inventory.append(item)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name

    def is_alive(self):
        return self.hp > 0

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        if isinstance(damage, int) and damage >= 0:
            self._damage = damage
        else:
            raise ValueError("Damage must be a positive integer.")

    # CRUD methods
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY,
                name TEXT,
                hp INTEGER 
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO players (id, name, hp)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.id, self.name, self.hp))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).ALL[self.id] = self

    def update(self):
        sql = """
            UPDATE players
            SET name = ?, hp = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.hp, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM players
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, name, hp):
        player = cls(name, hp)
        player.save()
        return player

    @classmethod
    def instance_from_db(cls, row):
        player = cls.all.get(row[0])
        if player:
            player.name = row[1]
            player.hp = row[2]
        else:
            player = cls(row[1], row[2])
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM players
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM players
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
