class Hunter:
    def hunt(self, lion):
        lion.roar()


class WildDog:
    def bark(self):
        print("bark")


class WildDogAdapter:
    def __init__(self, dog):
        self.dog = dog

    def roar(self):
        self.dog.bark()


Hunter().hunt(WildDogAdapter(WildDog()))
