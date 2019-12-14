"""This is bullets for static bots
    Put correct image for bullet!
"""

from PIL import Image


class Bullet:

    def __init__(self, x):
        self.x = x
        self.sprite = Image.open("graphics/sprites/policeman_sprites/policeman_right_static.png")
        self.vx = -3
        self.shoot_range = 30
        self.live = 30

    def move(self):
        """At this version bullets doesn't disappear, they just stop"""
        if self.live:
            self.x += self.vx
            self.live -= 1



