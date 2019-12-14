"""This class will operate in level coordinate system (x, y), point (0,0) on the left top side of the level"""
from ai.class_Simple import Simple
from PIL import Image
from ai.class_Smart import Smart

class Dog(Smart):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.sprite = Image.open("graphics/sprites/policeman_sprites/policeman_right_static.png")
