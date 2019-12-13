"""This class will operate with coordinate system (x, y), point (0,0) on the left top side of the level

"""

from classes.class_Camera import Camera


class Level:

    def __init__(self, canvas, length, player, platforms, enemies):
        self.canvas = canvas
        self.length = length  # Length of the level in coordinates units
        self.camera = Camera(canvas, player, platforms, enemies)
        self.player = player
        self.platforms = platforms
        self.enemies = enemies
        self.end_level = False

    def check_for_platform(self, object, check_x=True):
        on_platform = False
        for platform in self.platforms:
            end_loop = False
            # check for platform on the left
            if check_x and (platform.x + platform.width > object.x + object.vx > platform.x + platform.width / 2) and \
                    (
                            platform.y + platform.height > object.y > platform.y or
                            platform.y + platform.height > object.y + object.height > platform.y):
                end_loop = True
                object.push_x = True
                object.vx = (platform.x + platform.width) - object.x
            # check for platform on the right
            if check_x and (platform.x + platform.width / 2 > object.x + object.width + object.vx > platform.x) and \
                    (
                            platform.y + platform.height > object.y > platform.y or
                            platform.y + platform.height > object.y + object.height > platform.y):
                object.push_x = True
                object.vx = (object.x + object.width) - platform.x
                end_loop = True
            # check for platform below
            if (platform.y + platform.height / 2 >= object.y + object.height + object.vy >=
                platform.y) \
                    and ((platform.x + platform.width >= object.x + object.vx >= platform.x) or
                         (
                                 platform.x + platform.width >= object.x + object.width + object.vx >=
                                 platform.x)) and object.vy >= 0:
                end_loop = True
                on_platform = True
                if object.vy != 0:
                    object.vy = platform.y - (object.y + object.height)
                    object.push_on_platform = True
            # check for platform ahead
            if not end_loop and (platform.y + platform.height / 2 < object.y + object.vy <
                                 platform.y + platform.height) \
                    and ((platform.x + platform.width >= object.x + object.vx >= platform.x) or
                         (
                                 platform.x + platform.width >= object.x + object.width + object.vx >=
                                 platform.x)) and object.vy <= 0:
                end_loop = True
                if object.vy != 0:
                    object.vy = (platform.y + platform.height) - object.y
                    object.push_under_platform = True
                if end_loop:
                    break
        object.on_platform = on_platform

    def check_for_live(self):
        if self.player.y >= 800:
            return False
        for enemy in self.enemies:
            if (enemy.x <= self.player.x + self.player.width <= enemy.x + enemy.width or
                enemy.x <= self.player.x <= enemy.x + enemy.width) and \
                    enemy.y + enemy.height / 2 < self.player.y + self.player.height <= enemy.y + enemy.height:
                return False
        return True

    def check_for_end(self):
        """This method is for check if player end the level"""
        if self.player.x + self.player.width >= self.length:
            return True
        return False

    def game(self):
        """Main method of each level game, is called every 16 ms"""
        self.check_for_platform(self.player)
        self.player.move()
        self.camera.update()
        for enemy in self.enemies:
            self.check_for_platform(enemy, False)
            enemy.move()
        if self.check_for_end():
            self.camera.end_level()
            self.end_level = True
