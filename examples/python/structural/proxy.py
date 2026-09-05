class Door:
    def open(self):
        print("Opening door")


class Security:
    def __init__(self, door, password):
        self.door = door
        self.password = password

    def open(self, password):
        if password == self.password:
            self.door.open()
        else:
            print("Access denied")


Security(Door(), "secret").open("secret")
