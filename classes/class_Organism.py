"""It is the template class for all organisms in the game (except player)"""
from random import choice


class Organism:

    def __init__(self, x, y, width, height):
        self.x = x  # It is coordinates in natural coordinate system (not canvas coordinate system)
        self.y = y
        self.width = width
        self.height = height
        self.sprite = ""
        self.vx = choice([3, -3])
        self.vy = 0
