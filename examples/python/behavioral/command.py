class Bulb:
    def turn_on(self):
        print("Bulb is on")

    def turn_off(self):
        print("Bulb is off")


class TurnOn:
    def __init__(self, bulb):
        self.bulb = bulb

    def execute(self):
        self.bulb.turn_on()


class TurnOff:
    def __init__(self, bulb):
        self.bulb = bulb

    def execute(self):
        self.bulb.turn_off()


bulb = Bulb()
TurnOn(bulb).execute()
TurnOff(bulb).execute()
