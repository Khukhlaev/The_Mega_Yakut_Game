"""This class will operate only with normal coordinate system (x, y), point (0,0) on the left bottom side of the level

"""
from time import sleep


from classes.class_Camera import Camera


class Level:

    def __init__(self, canvas, length, player, platforms, enemies):
        self.canvas = canvas
        self.length = length  # Length of the level in coordinates units??
        self.camera = Camera(canvas, player, platforms, enemies)
        self.player = player
        self.platforms = platforms
        self.enemies = enemies
        self.end_level = False

    def check_for_end(self):
        pass

    def bind_all(self):
        self.canvas.bind("<KeyPress>", self.key_interpretator)
        self.canvas.bind("<KeyRelease>", self.key_release)

    def key_interpretator(self, event):
        if event.keycode == 39:
            self.player.vx = 5
        if event.keycode == 37:
            self.player.vx = -5

    def key_release(self, event):
        self.player.vx = 0

    def game(self):
        self.bind_all()
        while not self.end_level:
            self.player.move()
            self.camera.update()
            sleep(0.03)
