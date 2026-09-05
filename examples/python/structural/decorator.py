class SimpleCoffee:
    def get_cost(self):
        return 10

    def get_description(self):
        return "simple coffee"


class MilkCoffee:
    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost() + 2

    def get_description(self):
        return self.coffee.get_description() + ", milk"


coffee = MilkCoffee(SimpleCoffee())
