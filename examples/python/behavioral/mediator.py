class ChatRoom:
    def show_message(self, user, message):
        print(f"{user.name}: {message}")


class User:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def send(self, message):
        self.room.show_message(self, message)


room = ChatRoom()
User("Alice", room).send("Hello!")
