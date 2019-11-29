"""This class will operate with coordinate system (x, y), point (0,0) on the left top side of the level

"""

from physics.physics import gravity


# class body
class Player:
    def __init__(self, x, y, width, height):
        """
        PLayer class constructor
        Args:
            (x, y) - coordinates of the top left point of the rectangle in which the model is enclosed
            height, width - height and width of this rectangle
        """
        self.live = True
        self.x = x  # It is coordinates in natural coordinate system (not canvas coordinate system)
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0
        self.vy = 0
        self.on_platform = True

    def move(self):
        self.vy = gravity(self.vy, self.on_platform)
        self.x += self.vx
        self.y += self.vy

    def move_left(self):
        self.vx = -5

    def move_right(self):
        self.vx = 5
