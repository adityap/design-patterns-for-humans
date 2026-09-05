from abc import ABC, abstractmethod


class Door(ABC):
    @abstractmethod
    def description(self):
        pass


class WoodenDoor(Door):
    def description(self):
        return "wooden door"


class DoorFittingExpert(ABC):
    @abstractmethod
    def description(self):
        pass


class Carpenter(DoorFittingExpert):
    def description(self):
        return "carpenter"


class DoorFactory(ABC):
    @abstractmethod
    def make_door(self):
        pass

    @abstractmethod
    def make_fitting_expert(self):
        pass


class WoodenDoorFactory(DoorFactory):
    def make_door(self):
        return WoodenDoor()

    def make_fitting_expert(self):
        return Carpenter()


factory = WoodenDoorFactory()
print(factory.make_door().description())
print(factory.make_fitting_expert().description())
