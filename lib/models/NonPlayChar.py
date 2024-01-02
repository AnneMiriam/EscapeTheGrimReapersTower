import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw Non Playable Character objects.")

    def __str__(self):
        return self.name
    
    
class Casper(NonPlayableCharacter):
    def __init__(self):
        self.name = "Ghost"
        self.inventory = [items.StaleBread(),
                          items.StaleBread(),
                          items.Rope(),
                        #   items.Key(),
                          items.MysteryLiquid()]