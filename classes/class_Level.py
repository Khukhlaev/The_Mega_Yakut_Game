"""This class will operate with coordinate system (x, y), point (0,0) on the left top side of the level

"""
from time import sleep

from classes.class_Camera import Camera


class Level:

    def __init__(self, root, canvas, length, player, platforms, enemies):
        self.root = root
        self.canvas = canvas
        self.length = length  # Length of the level in coordinates units
        self.camera = Camera(canvas, player, platforms, enemies)
        self.player = player
        self.platforms = platforms
        self.enemies = enemies
        self.end_level = False

    def check_for_platform(self):
        self.player.on_platform = False
        for platform in self.platforms:
            if (platform.y + platform.height / 2 >= self.player.y + self.player.height + self.player.vy >=
                platform.y - platform.height / 2) \
                    and ((platform.x + platform.width >= self.player.x + self.player.vx >= platform.x) or
                         (
                                 platform.x + platform.width >= self.player.x + self.player.width + self.player.vx >=
                                 platform.x)):
                if self.player.vy != 0:
                    self.player.vy = platform.y - (self.player.y + self.player.height)
                    self.player.push_on_platform = True
                self.player.on_platform = True
                break

    def check_for_end(self):
        if self.player.x >= self.length:
            print("The end!")

    def bind_all(self):
        self.root.bind("<KeyPress>", self.key_interpreter)
        self.root.bind("<KeyRelease>", self.key_release)

    def key_interpreter(self, event):
        if event.keycode == 39:
            self.player.move_right()
        if event.keycode == 37:
            self.player.move_left()
        if event.keycode == 38:
            self.player.jump()

    def key_release(self, event):
        self.player.vx = 0

    def game(self):
        self.bind_all()
        while not self.end_level:
            self.check_for_platform()
            self.player.move()
            self.camera.update()
            sleep(0.01667)
