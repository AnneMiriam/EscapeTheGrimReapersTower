
from models.__init__ import CURSOR, CONN
import random


class Enemy:
    ALL = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name
        self.hp = 5
        self.damage = 5
        self.alive_text = "Something otherworldly has appeared."
        self.dead_text = "The creature has gone back to it's realm."

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string.")

    
    # @property
    # def hp(self):
    #     return self._hp

    # @hp.setter
    # def hp(self, hp):
    #     if isinstance(hp, int):

    #         self._hp = hp
    #     else:
    #         raise ValueError("HP must be an integer.")

    # @property
    # def damage(self):
    #     return self._damage

    # @damage.setter
    # def damage(self, damage):
    #     if isinstance(damage, int) and damage > 0:
    #         self._damage = damage
    #     else:
    #         raise ValueError("Damage must be a positive integer.")

    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS enemies (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  hp INTEGER,
                  damage INTEGER)
              """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS enemies"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO enemies (name, hp, damage)
                 VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (self.name, self.hp, self.damage))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).ALL[self.id] = self

    def update(self):
        sql = """UPDATE enemies
                 SET name = ?, hp = ?, damage = ?
                 WHERE id = ?"""
        CURSOR.execute(sql, (self.name, self.hp, self.damage, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM enemies WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).ALL[self.id]
        self.id = None

    @classmethod
    def create(cls, name, hp, damage):
        """Initialize a new Enemy instance and save the object to the database"""
        enemy = cls(name, hp, damage)
        enemy.save()
        return enemy

    @classmethod
    def instance_from_db(cls, row):
        enemy = cls.ALL.get(row[0])
        if enemy:
            enemy.name = row[1]
            enemy.hp = row[2]
            enemy.damage = row[3]

        else:
            enemy = cls(row[1])
            enemy.hp = row[2]
            enemy.damage = row[3]
            enemy.id = row[0]
            cls.ALL[enemy.id] = enemy
        return enemy

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM enemies"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """SELECT * FROM enemies WHERE id = ?"""
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """SELECT * FROM enemies WHERE name is ?"""
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


class GrimReaper(Enemy):
    def __init__(self):
        self.name = "Grim Reaper"
        self.hp = 100
        self.damage = random.randint(10, 20)
        self.alive_text = "You have run into the Grim Reaper!"
        self.dead_text = "They are death! They cannot be killed!"


class BlackCat(Enemy):
    def __init__(self):
        self.name = "Black Cat"
        self.hp = 45
        self.damage = 2
        self.alive_text = "A Black Cat has crossed your path!"
        self.dead_text = "Rude! It was just walking by!"


class Poltergeist(Enemy):
    def __init__(self):
        self.name = "Ghost"
        self.hp = 10
        self.damage = random.randint(5, 10)
        self.alive_text = "You pissed off a Poltergeist!"
        self.dead_text = "Your exorcism succeeded!"


class BlackWidow(Enemy):
    def __init__(self):
        self.name = "Black Wider Spider"
        self.hp = 5
        self.damage = 4
        self.alive_text = "A Black Widow has bitten you."
        self.dead_text = "You squished it."
