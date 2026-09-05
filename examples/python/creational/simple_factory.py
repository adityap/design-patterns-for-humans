class WoodenDoor:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class DoorFactory:
    @staticmethod
    def make_door(width, height):
        return WoodenDoor(width, height)


door = DoorFactory.make_door(100, 200)
print(door.width, door.height)
