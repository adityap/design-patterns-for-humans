class President:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


president_one = President()
president_two = President()
assert president_one is president_two
