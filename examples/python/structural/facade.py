class Computer:
    def get_hard_drive(self):
        return "hard drive"

    def get_memory(self):
        return "memory"

    def get_processor(self):
        return "processor"


class ComputerFacade:
    def __init__(self, computer):
        self.computer = computer

    def get_configuration(self):
        return [self.computer.get_hard_drive(), self.computer.get_memory(), self.computer.get_processor()]


print(ComputerFacade(Computer()).get_configuration())
