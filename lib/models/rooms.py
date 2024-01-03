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
        return """
        You take another look around the room. You can see that the window opens up onto a small balcony. 
        """


class StairCase(MapRoom):
    def intro_text(self):
        return """
        The hinges of the door squeal as you open it, their infrequent use and lack of care made evident.
        Before you is a staircase, its walls and steps carved from the same stone as the attic room.
        It curves as it descends, spiralling ever downward into the great unknown. 
        As you descend, you come upon a door. It appears to be unlocked. 
        You count three more doors before the staircase opens at the bottom, a soft glow eminating from the room awaiting you there.
        """


class FourthFloorRoom(MapRoom):
    def intro_text(self):
        return """
        This room is similar to the attic room, cold and cave-like with stone floors and walls. It's smaller, though, and has no window.
        On the far wall you see a cot with an old mattress on top of it, speckled with mold, its stuffing coming out of several holes.
        You can see words scratched onto the wall next to the cot - on closer inspection, they read NO ONE ESCAPES DEATH
        """


class ThirdFloorRoom(MapRoom):
    def intro_text(self):
        return """
        You find another small room. Like the attic room, this one has a window that leads out to a small balcony.
        The room is otherwise bare, save for the candle wax pooling in the center of the floor beneath the lantern.
        """


class SecondFloorRoom(MapRoom):
    def intro_text(self):
        return """
        This room is much like the others, although considerably less empty. 
        A threadbare rug covers the floor, its red and orange hues nearly entirely washed out by years of wear and tear.
        A wingback armchair sits in the corner, crushed velvet upholstery worn smooth on the seat and back.
        On the far wall is a small wooden writing desk with one drawer. 
        """


class FirstFloorRoom(MapRoom):
    def intro_text(self):
        return """
        The smell of rot greets you as you open the door. 
        Crates of what must have once been fruit are stacked haphazardly in the corners, sticky liquid seeping out from the edges.
        Shelves filled with wine bottles, all either smashed or lying open on their side, line the walls.
        The cracked window on the far side of the room is doing nothing to help the smell. 
        Or maybe it is, although you cannot imagine it getting worse than this.
        """


class WindowOption(MapRoom):
    def intro_text(self):
        return """"""


class EntryWay(MapRoom):
    def intro_text(self):
        return """
        You reach the bottom of the stairs and are greeted by a yawning entryway, its high walls lined with iron lanterns holding flickering candles.
        Before you are a set of heavy double doors, stained a rich reddish-brown, intricately carved with scenes of mortals fleeing in terror from a skeletal figure in billowing robes wielding a scythe.
        The path that leads to the doors is lined with statues of similar skeletal figures.
        Though they have no eyes, you could swear you can feel them watching you.
        """


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

    # def __init__(self, x, y):
    #     self.trader
    #     super().__init__(x, y)
