"""This class is responsible for bot which will follow player. For correct work firstly check for player, than move"""
from classes.class_Organism import Organism
from physics.physics import gravity


class Smart(Organism):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.on_place = False
        self.on_platform = False
        self.push_on_platform = False  # True if we need to push player clearly on platform if he will go into it
        self.push_under_platform = False
        self.counter = 0  # counter to understand if bot has jumped from platform
        self.dist = 0  # current distance from start
        self.max = 150  # max distance from start
        self.vision = 150  # max distance to react on player
    def move(self):
        if self.on_platform:
            self.on_place = True
            self.counter += 1
            if self.dist >= self.max:
                self.vx = -self.vx
                self.dist = 0
                self.max = 150
        if not self.on_place and (self.counter % 2 == 0):
            self.vy = gravity(self.vy, self.on_platform)
        elif not self.on_platform and (self.counter % 2 != 0):
            self.vy = -10
            self.on_place = False
            self.counter += 1
        self.x += self.vx
        self.y += self.vy
        self.dist += 1

    def check_for_player(self, Player):
        """This method detects player and make bot moving towards him"""
        if (self.x - Player.x)**2 <= self.vision**2:
            self.vx = 5*(Player.x - self.x)/abs(Player.x - self.x)
        else:
            self.vx = 0