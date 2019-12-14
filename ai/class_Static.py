"""This class defines static bot's actions"""
"""They shoot only to the left"""
from classes.class_Organism import Organism
from objects.class_Player import Player
from objects.class_Bullet import import Bullet

class Static(Organism):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.on_place = False
        self.on_platform = False
        self.push_on_platform = False  # True if we need to push player clearly on platform if he will go into it
        self.push_under_platform = False
        self.shoot_range = 30

    def shoot(self):
        """Shoot if player is in shoot range higher than bot, but there is no limit for number of bullet
         but there is no limit for number of bullets? that means that a new bullet will creats each iteration """
        if (self.x - Player.x <= Bullet.shoot_range) and (Player.y - self.y >= 0):
            new_bullet = Bullet()
