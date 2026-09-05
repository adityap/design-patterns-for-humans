class EditorMemento:
    def __init__(self, content):
        self.content = content


class Editor:
    def __init__(self):
        self.content = ""

    def type(self, words):
        self.content += words

    def save(self):
        return EditorMemento(self.content)

    def restore(self, memento):
        self.content = memento.content


editor = Editor()
editor.type("First version")
saved = editor.save()
editor.type(" with changes")
editor.restore(saved)
print(editor.content)
