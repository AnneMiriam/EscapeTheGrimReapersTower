import random
from models.Enemy import Enemy, BlackCat, BlackWidow, Poltergeist, GrimReaper
# from data.default_enemies import default_enemies
from models.NonPlayChar import *
from models.__init__ import CURSOR, CONN


class MapRoom:
    def __init__(self):
        pass

    def intro_text(self):
        raise NotImplementedError("")
    
    def return_text(self):
        raise NotImplementedError("")

    def modify_player(self, player):
        pass


class AtticRoom(MapRoom):
    def intro_text(self):
        return """You take another look around the room. You can see that the window opens up onto a small balcony."""
    def return_text(self):
        return """The same cold, empty room you started in. On one side stands a plain wooden door. On the other, a window that looks as if it's about to be blown off its hinges."""

class AtticRoomWindow(MapRoom):
    def intro_text(self): 
        return """The window shakes violently as you approach, the wind outside whipping up into a frenzy. The balcony is soaking wet from the rain, and as you peer over the edge you realize you cannot see the ground. You can, however, see another small balcony a few floors below you."""

class StairCase(MapRoom):
    def intro_text(self):
        return """The hinges of the door squeal as you open it, their infrequent use and lack of care made evident. Before you is a staircase, its walls and steps carved from the same stone as the attic room. It curves as it descends, spiralling ever downward into the great unknown.\nAs you descend, you come upon a door. It appears to be unlocked. You count three more doors before the staircase opens at the bottom, a soft glow eminating from the room awaiting you there."""
    def return_text(self):
        return """You return to the staircase. Where else can you go?"""

class FourthFloorRoom(MapRoom):
    def intro_text(self):
        return """This room is similar to the attic room, cold and cave-like with stone floors and walls. It's smaller, though, and has no window. On the far wall you see a cot with an old mattress on top of it, speckled with mold, its stuffing coming out of several holes.\nYou can see words scratched onto the wall next to the cot - on closer inspection, they read NO ONE ESCAPES DEATH"""


class ThirdFloorRoom(MapRoom):
    def intro_text(self):
        return """You find another small room. Like the attic room, this one has a window that leads out to a small balcony.\nThe room is otherwise bare, save for the candle wax pooling in the center of the floor beneath the lantern.
        """

class ThirdFloorWindow(MapRoom):
    def intro_text(self):
        return """The wind howls, spraying you with droplets of rain, thoroughly soaking your clothes. It's still too dark and stormy to see the bottom of the tower, but below you you can see another balcony. Above you, you see the balcony that must lead to the attic room."""


class SecondFloorRoom(MapRoom):
    def intro_text(self):
        return """This room is much like the others, although considerably less empty.\nA threadbare rug covers the floor, its red and orange hues nearly entirely washed out by years of wear and tear. A wingback armchair sits in the corner, crushed velvet upholstery worn smooth on the seat and back.\nOn the far wall is a small wooden writing desk with one drawer. 
        """


class FirstFloorRoom(MapRoom):
    def intro_text(self):
        return """The smell of rot greets you as you open the door. Crates of what must have once been fruit are stacked haphazardly in the corners, sticky liquid seeping out from the edges. Shelves filled with wine bottles, all either smashed or lying open on their side, line the walls. The cracked window on the far side of the room is doing nothing to help the smell. Or maybe it is, although you cannot imagine it getting worse than this.
        """


class WindowOption(MapRoom):
    def intro_text(self):
        return """"""


class EntryWay(MapRoom):
    def intro_text(self):
        return """You reach the bottom of the stairs and are greeted by a yawning entryway, its high walls lined with iron lanterns holding flickering candles. Before you are a set of heavy double doors, stained a rich reddish-brown, intricately carved with scenes of mortals fleeing in terror from a skeletal figure in billowing robes wielding a scythe. The path that leads to the doors is lined with statues of similar skeletal figures.\nThough they have no eyes, you could swear you can feel them watching you.
        """


class VictoryIsYours(MapRoom):
    def intro_text(self):
        return """You have DEFEATED the GRIM REAPER!"""

    def modify_player(self, player):
        player.victory = True


class EnemyAndFriends(MapRoom):
    def __init__(self):
        r = random.random()

        if r < 0.40:
            self.enemy = BlackCat()
            self.alive_text = "A Black Cat has crossed your path!"
            self.dead_text = "Rude! It was just walking by!"

        elif r < 0.60:
            self.enemy = BlackWidow()
            self.alive_text = "A Black Widow has bitten you."
            self.dead_text = "You squished it."

        elif r < 0.80:
            self.enemy = Poltergeist()
            self.alive_text = "You pissed off a Poltergeist!"
            self.dead_text = "Your exorcism succeeded!"

        else:


            self.enemy = GrimReaper()

            self.alive_text = "You have run into the Grim Reaper!"
            self.dead_text = "They are death! They cannot be killed!"

        super().__init__(self)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text
      

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(
                "Enemy does {} damage. You have {} HP remaining.".format(
                    self.enemy.damage, player.hp
                )
            )


class TradingGhost(MapRoom):
    def intro_text(self):
        return """
        With a start, you realize you are not alone. 
        In the center of the room floats an old woman, her translucent feet not hovering just an inch off the ground.
        Her bony hands grip the sides of a knitted shawl that she seems to be appraising. 
        As you approach, she looks up at you with a warm smile. 
        "Oh! Hello dearie," she says. "It's been a long time since I had a visitor! 
        My name is Margaret and I am the purveyor of the finest goods this tower has to offer. Of course,"
        she chuckles lightly, "that isn't always saying much. I would be happy to part with any of my wares
        for the right price!" Her smile droops a bit, and her eyes take on a pitying look. "However, I must warn you, 
        my prices may not be to your liking. I can only deal in life, you see. It's the only thing with real 
        value around here. But, if you're willing to part with just a sip of your vitality, I can give you anything you please,
        anything at all!"
        She looks at you expectantly. 
        """

    def __init__(self):
        self.trader = Casper()
        super().__init__(self)

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
