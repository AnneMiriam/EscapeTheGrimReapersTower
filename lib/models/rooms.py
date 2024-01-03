import random
from enemy import Enemy
from data.default_enemies import default_enemies


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
        if r < 0.30:
            self.enemy = default_enemies[1]
            self.alive_text = "A Black Cat has crossed your path!"
            self.dead_text = "Rude! It was just walking by!"

        elif r < 0.50:
            self.enemy = default_enemies[3]
            self.alive_text = "A Black Widow has bitten you."
            self.dead_text = "You squished it."

        elif r < 0.80:
            self.enemy = default_enemies[2]
            self.alive_text = "You pissed off a Poltergeist!"
            self.dead_text = "Your exorcism succeeded!"

        else:
            self.enemy = default_enemies[0]
            self.alive_text = "You have run into the Grim Reaper!"
            self.dead_text = "They are death! They cannot be killed!"

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
