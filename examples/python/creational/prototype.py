from copy import copy


class Sheep:
    def __init__(self, name, category="Mountain Sheep"):
        self.name = name
        self.category = category


original = Sheep("Jolly")
cloned = copy(original)
cloned.name = "Dolly"
