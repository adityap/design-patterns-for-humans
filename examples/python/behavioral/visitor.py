class Animal:
    def accept(self, visitor):
        visitor.visit(self)


class SpeakVisitor:
    def visit(self, animal):
        print(f"Visiting {animal.__class__.__name__}")


Animal().accept(SpeakVisitor())
