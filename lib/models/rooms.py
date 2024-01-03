import random
import Enemy
import NonPlayChar
from models.__init__ import CURSOR, CONN


class MapRoom:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("")

    def modify_player(self, player):
        pass


class AtticRoom(MapRoom):
    def intro_text(self):
        return """"""


class StairCase(MapRoom):
    def intro_text(self):
        return """"""


class RandomRoom(MapRoom):
    def intro_text(self):
        return """"""


class WindowOption(MapRoom):
    def intro_text(self):
        return """"""


class EntryWay(MapRoom):
    def intro_text(self):
        return """"""


class VictoryIsYours(MapRoom):
    def intro_text(self):
        return """You have DEFEATED the GRIM REAPER!"""

    def modify_player(self, player):
        player.victory = True


class EnemyAndFriends(MapRoom):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = Enemy.BlackCat()
            self.alive_text = ""
            self.dead_text = ""

        elif r < 0.75:
            self.enemy = Enemy.Poltergeist()
            self.alive_text = ""
            self.dead_text = ""

        elif r < 0.90:
            # self.enemy = enemies.?()
            self.alive_text = ""
            self.dead_text = ""

        else:
            self.enemy = Enemy.GrimReaper()
            self.alive_text = ""
            self.dead_text = ""

        super().__init__(x, y)

    # def intro_text(self):
    #     text = self.alive_text if self.enemy.alive() else self.dead_text
    #     return text

    # def modify_player(self, player):
    #     if self.enemy.alive():
    #         player.hp = player.hp - self.enemy.damage
    #         print(
    #             "Enemy does {} damage. You have {} HP remaining.".format(
    #                 self.enemy.damage, player.hp
    #             )
    #         )


class TradingGhost(MapRoom):
    def intro_text(self):
        return """You see something lurking, I think it wants to trade???"""

    def __init__(self, x, y):
        self.trader = NonPlayChar.Casper()
        super().__init__(x, y)

    def trade(self, consumer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} HP".format(i, item.name, item.healing_value))
        while True:
            user_input = input("Select your item or press q to exit")
            if user_input in ["q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    exchange = seller.inventory[choice - 1]
                    self.transaction(seller, consumer, exchange)
                except ValueError:
                    print("Unacceptable selection!")

    def transaction(self, seller, consumer, item):
        if item.healing_value > consumer.hp:
            print("you are lacking in vitality, your HP is insufficient.")
            return
        seller.inventory.remove(item)
        consumer.inventory.append(item)
        seller.hp = seller.hp + item.healing_value
        consumer.hp = seller.hp - item.healing_value
        print("Trade sealed in ethereal terms.")

    def trading(self, player):
        print("Would you like to test your fate? (t)rade or (q)uit")
        user_input = input()
        if user_input in ["q"]:
            return
        elif user_input in ["t"]:
            print("Behold, these are the offerings for trade from beyond the veil.")
            self.trade(consumer=player, seller=self.trader)
        else:
            print("Unacceptable selection!")
