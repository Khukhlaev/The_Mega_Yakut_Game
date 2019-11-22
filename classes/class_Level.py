from objects.class_Platform import Platform


class Level:

    def __init__(self, canvas, length, platforms, person):
        self.canvas = canvas
        self.length = length  # Length of the level in coordinates units??
        self.platforms = platforms
        self.person = person
        self.end_level = False

    def draw_all(self, velocity):
        pass

    def change_coords(self):
        pass

    def cadre(self):
        self.change_coords()
        self.draw_all()

    def game(self):
        while not self.end_level:
            pass
