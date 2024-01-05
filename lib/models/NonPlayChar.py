from models.items import *


class NonPlayableCharacter:
    def __init__(self, name):
        self.name = name
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name


class Casper(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.inventory = [
            StaleBread(),
            MoldyApple(),
            MysteriousLiquid(),
            QuestionableLiquid(),
        ]
