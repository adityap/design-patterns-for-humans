class Phone:
    def __init__(self):
        self.state = IdleState()

    def pick_up(self):
        self.state.pick_up(self)

    def hang_up(self):
        self.state.hang_up(self)


class IdleState:
    def pick_up(self, phone):
        print("Phone picked up")
        phone.state = CallingState()

    def hang_up(self, phone):
        print("Phone is already idle")


class CallingState:
    def pick_up(self, phone):
        print("Already calling")

    def hang_up(self, phone):
        print("Call ended")
        phone.state = IdleState()


phone = Phone()
phone.pick_up()
phone.hang_up()
