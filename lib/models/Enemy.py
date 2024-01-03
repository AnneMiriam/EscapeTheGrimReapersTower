from models.__init__ import CURSOR, CONN

import random


class Enemy:
    all = {}

    def __init__(self, type, hp, damage, name=None, id=None):
        self.id = id
        self.name = name
        self.type = type
        self.hp = hp
        self.damage = damage

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string.")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise ValueError("Type must be a string.")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if isinstance(hp, int) and hp >= 0:
            self._hp = hp
        else:
            raise ValueError("HP must be a positive integer.")

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def hp(self, damage):
        if isinstance(damage, int) and damage >= 0:
            self._damage = damage
        else:
            raise ValueError("Damage must be a positive integer.")

    @classmethod
    def create_table(cls):
        sql = """ CREATE TABLE IF NOT EXISTS enemies (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  type TEXT,
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
        sql = """INSERT INTO enemies (name, type, hp, damage)
                 VALUES (?, ?, ?, ?)"""
        CURSOR.execute(sql, (self.name, self.type, self.hp, self.damage))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).ALL[self.id] = self

    def update(self):
        sql = """UPDATE enemies
                 SET name = ?, type = ?, hp = ?, damage = ?
                 WHERE id = ?"""
        CURSOR.execute(sql, (self.name, self.type, self.hp, self.damage, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM enemies WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).ALL[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        enemy = cls.ALL.get(row[0])
        if enemy:
            enemy.name = row[1]
            enemy.type = row[2]
            enemy.hp = row[3]
            enemy.damage = row[4]
        else:
            enemy = cls(row[1], row[2], row[3], row[4])
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


class GrimReaper(Enemy):
    def __init__(self, room):
        self.name = "The Grim Reaper"
        self.type = "boss"
        self.hp = 50
        self.damage = random.randint(10, 20)
        self.room = room


class BlackCat(Enemy):
    def __init__(self):
        self.name = "Black Cat"
        self.hp = 9
        self.damage = 2


class Poltergeist(Enemy):
    def __init__(self):
        self.name = "Ghost"
        self.hp = 10
        self.damage = random.randint(5, 10)
