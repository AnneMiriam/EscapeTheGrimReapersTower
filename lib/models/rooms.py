
from models.enemy import Enemy, BlackCat, BlackWidow, Poltergeist, GrimReaper

# from data.default_enemies import default_enemies
from models.NonPlayChar import Casper
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
        return """You take another look around the room. You can see that the window opens up onto a small balcony. In the corner of the room lies a large book bound in red leather with the words "Tome of Souls" emblazoned across the front in flakey gold lettering."""

    def return_text(self):
        return """The same cold, empty room you started in. On one side stands a plain wooden door. On the other, a window that looks as if it's about to be blown off its hinges."""


class AtticRoomWindow(MapRoom):
    def intro_text(self):
        return """The window shakes violently as you approach, the wind outside whipping up into a frenzy. The balcony is soaking wet from the rain, and as you peer over the edge you realize you cannot see the ground. You can, however, see another small balcony a few floors below you."""


class StairCase(MapRoom):
    def intro_text(self):
        return """The hinges of the door squeal as you open it, their infrequent use and lack of care made evident. Before you is a staircase, its walls and steps carved from the same stone as the attic room. It curves as it descends, spiralling ever downward into the great unknown. At the top of the stairs, the shimmering, translucent form of an old woman hums to herself quietly. She seems to pay you no mind.\nAs you descend, you come upon a door. It appears to be unlocked. You count three more doors before the staircase opens at the bottom, a soft glow emanating from the room awaiting you there."""

    def return_text(self):
        return """You return to the staircase. Where else can you go?"""


class FourthFloorRoom(MapRoom):
    def intro_text(self):
        return """This room is similar to the attic room, cold and cave-like with stone floors and walls. It's smaller, though, and has no window. On the far wall you see a cot with an old mattress on top of it, speckled with mold, its stuffing coming out of several holes.\nYou can see words scratched onto the wall next to the cot - on closer inspection, they read NO ONE ESCAPES DEATH"""


class ThirdFloorRoom(MapRoom):
    def intro_text(self):
        return """You find another small bedroom. Like the attic room, this one has a window that leads out to a small balcony.\nThe frame of the bed in the corner looks ancient, its once fine details chipped and splintering. The mattress is lumpy and old, but looks dry and useable.\nCandle wax pools in the center of the floor beneath the lantern, the candle within having tipped over who knows how long ago.
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


class FirstFloorWindow(MapRoom):
    def intro_text(self):
        return """The wind seems to be less fierce down here. The rain, also, seems lighter. It's still dark, but you think you can finally see the bottom of the tower. Above you, you see the balcony that must lead to the third floor room."""


class WindowOption(MapRoom):
    def intro_text(self):
        return """"""


class EntryWay(MapRoom):
    def intro_text(self):
        return """You reach the bottom of the stairs and are greeted by a yawning entryway, its high walls lined with iron lanterns holding flickering candles. Before you are a set of heavy double doors, stained a rich reddish-brown, intricately carved with scenes of mortals fleeing in terror from a skeletal figure in billowing robes wielding a scythe. The path that leads to the doors is lined with statues of similar skeletal figures.\nThough they have no eyes, you could swear you can feel them watching you.
        """

    def return_text(self):
        return """The grandeur of the entryway is matched only by its eeriness. The double doors stand before you, silent and firm, and you can't help but empathize with the mortals carved on their faces."""


class VictoryIsYours(MapRoom):
    def intro_text(self):
        return """You have DEFEATED the GRIM REAPER!"""

    def modify_player(self, player):
        player.victory = True


class TradingGhost(MapRoom):
    def __init__(self):
        self.trader = Casper()

    def intro_text(self):
        return """With a start, you realize you are not alone.\nAt the top of the stairs floats an old woman, her translucent feet hovering just an inch off the ground. Her bony hands grip the sides of a knitted shawl that she seems to be appraising. As you approach, she looks up at you with a warm smile. \n"Oh! Hello dearie," she says. "It's been a long time since I had a visitor! My name is Margaret and I am the purveyor of the finest goods this tower has to offer. Of course," she chuckles lightly, "that isn't always saying much. I would be happy to part with any of my wares for the right price!" \nHer smile droops a bit, and her eyes take on a pitying look. \n"However, I must warn you, my prices may not be to your liking. I can only deal in life, you see. It's the only thing with real value around here. But, if you're willing to part with just a sip of your vitality, I can give you anything you please, anything at all!" \nShe looks at you expectantly. 
        """
