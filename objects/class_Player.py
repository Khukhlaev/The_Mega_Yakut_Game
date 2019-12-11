"""This class will operate with coordinate system (x, y), point (0,0) on the left top side of the level

"""

from PIL import Image, ImageTk
from physics.physics import gravity


delay = 0


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
        self.sprite = Image.open("graphics/sprites/player_static_right.png")
        self.on_platform = False
        self.push_on_platform = False  # True if we need to push player clearly on platform if he will go into it
        self.push_under_platform = False

    def move(self):
        if not self.push_on_platform:
            self.vy = gravity(self.vy, self.on_platform)
        self.x += self.vx
        self.y += self.vy

    def move_left(self):
        self.vx = -5

    def move_right(self):
        self.vx = 5

    def jump(self):
        self.on_platform = False
        self.vy = -5

    def set_sprite(self):
        global delay
        if self.vx == 0 or delay == 5:
            delay = 0
        if self.vx != 0:
            if self.vx > 0:
                if delay <= 2.5:
                    self.sprite = Image.open("graphics/sprites/player_static_right.png")
                else:
                    self.sprite = Image.open("graphics/sprites/player_running_right_1.png")
            else:
                if delay <= 2.5:
                    self.sprite = Image.open("graphics/sprites/player_static_left.png")
                else:
                    self.sprite = Image.open("graphics/sprites/player_running_left_1.png")
            delay += 0.5
