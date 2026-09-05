class DarkTheme:
    def get_color(self):
        return "Dark black"


class AboutPage:
    def __init__(self, theme):
        self.theme = theme

    def get_content(self):
        return f"About page in {self.theme.get_color()}"


page = AboutPage(DarkTheme())
print(page.get_content())
