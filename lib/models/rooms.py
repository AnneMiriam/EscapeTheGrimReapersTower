import random


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
            # self.enemy = enemies.BlackCat()
            self.alive_text = ""
            self.dead_text = ""

        elif r < 0.75:
            # self.enemy = enemies.?()
            self.alive_text = ""
            self.dead_text = ""

        elif r < 0.90:
            # self.enemy = enemies.?()
            self.alive_text = ""
            self.dead_text = ""

        else:
            # self.enemy = enemies.GrimReaper()
            self.alive_text = ""
            self.dead_text = ""

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.alive():
            player.hp = player.hp - self.enemy.damage
            print("".format(self.enemy.damage, player.hp))


class TradingGhost(MapRoom):
    def intro_text(self):
        return """You see something lurking, I think it wants to trade???"""

    # def __init__(self, x, y):
    #     self.trader
    #     super().__init__(x, y)
