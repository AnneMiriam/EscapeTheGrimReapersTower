from models.items import *


class NonPlayableCharacter:
    def __init__(self):
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name


class Casper(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.inventory = [
            StaleBread(),
            Rope(),
            MysteriousLiquid(),
        ]
