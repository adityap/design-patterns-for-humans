class Tea:
    def __init__(self, flavor):
        self.flavor = flavor


class TeaFactory:
    _teas = {}

    @classmethod
    def get_tea(cls, flavor):
        cls._teas.setdefault(flavor, Tea(flavor))
        return cls._teas[flavor]


first = TeaFactory.get_tea("green")
second = TeaFactory.get_tea("green")
assert first is second
