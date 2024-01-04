class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class StaleBread(Consumable):
    def __init__(self):
        self.name = "Stale bread"
        self.description = "The bread is old and hard, but still edible - you wonder how long it's been there."
        self.healing_value = 5


class QuestionableLiquid(Consumable):
    def __init__(self):
        self.name = "Questionable liquid"
        self.description = "A vial filled with a black, viscous liquid. It gives off a cloying, sickly smell like garbage on a hot afternoon."
        self.healing_value = -5


class MoldyApple(Consumable):
    def __init__(self):
        self.name = "Moldy apple"
        self.description = "A small, fuzzy green ball in the shape of an apple. You probably should not eat that."
        self.healing_value = -5


class MysteriousLiquid(Consumable):
    def __init__(self):
        self.name = "Mysterious liquid"
        self.description = "A vial filled with a golden liquid with an almost iridescent sheen to it. It smells a bit like caramel."


class Usable:
    def __init__(self):
        raise NotImplementedError("Do not create raw usable objects.")

    def __str__(self):
        return self.name


class Rope(Usable):
    def __init__(self):
        self.name = "Rope"
        self.description = ""
