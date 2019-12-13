"""This class is responsible for the bot actions"""

class Dumb:

    def __init__(self, x, y, width, height):
        self.x = x  # It is coordinates in natural coordinate system (not canvas coordinate system)
        self.y = y
        self.x_abstract = x
        self.y_abstract = y
        self.width = width
        self.height = height
        self.vx = 0
        self.vy = 0
        self.on_platform = False
        self.platform_beside = False


    def move(self):
        if self.on_platform and self.x + self.vx: pass