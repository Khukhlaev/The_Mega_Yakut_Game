"""It is the template class for all organisms in the game"""
from random import choice


class Organism:

    def __init__(self, x, y, width, height):
        self.x = x  # It is coordinates in natural coordinate system (not canvas coordinate system)
        self.y = y
        self.live = True
        self.width = width
        self.height = height
        self.sprite = ""
        self.vx = choice([-5, -5])
        self.vy = 0
        self.vision = 150  # max distance to react on player
    def check_for_player(self, Player):
        """This method detects player and make bot moving towards him"""
        if (self.x - Player.x)**2 <= self.vision**2:
            self.vx = 5*(Player.x - self.x)/abs(Player.x - self.x)
        else:
            self.vx = 0

