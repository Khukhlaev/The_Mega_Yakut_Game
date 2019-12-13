"""This class will operate with coordinate system (x, y), point (0,0) on the left top side of the level

"""

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

    def check_for_platform(self, object):
        on_platform = False
        for platform in self.platforms:
            end_loop = False
            # check for platform on the left
            if (platform.x + platform.width > object.x + object.vx > platform.x + platform.width / 2) and \
                    (
                            platform.y + platform.height > object.y > platform.y or
                            platform.y + platform.height > object.y + object.height > platform.y):
                end_loop = True
                object.push_x = True
                object.vx = (platform.x + platform.width) - object.x
            # check for platform on the right
            if (platform.x + platform.width / 2 > object.x + object.width + object.vx > platform.x) and \
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

    def check_for_death(self):
        if self.player.y >= 650:
            self.player.live = False
        for enemy in self.enemies:
            if enemy[0].x + enemy[0].width / 2 < self.player[0].x < enemy[0].x + enemy[0].width and \
                    enemy[0].y + enemy[0].height / 2 < self.player[0].y < enemy[0].y + enemy[0].height:
                self.player.live = False

    def check_for_end(self):
        """This method is for check if player end the level"""
        if self.player.x + self.player.width >= self.length:
            return True
        return False

    def bind_all(self):
        self.root.bind("<KeyPress>", self.key_interpreter)
        self.root.bind("<KeyRelease>", self.key_release)

    def key_interpreter(self, event):
        if event.keycode == 39:
            self.player.move_right()
        if event.keycode == 37:
            self.player.move_left()
        if event.keycode == 38 and self.player.on_platform:
            self.player.jump()

    def key_release(self, event):
        if event.keycode == 39 or event.keycode == 37:
            self.player.vx = 0

    def game(self):
        """Main method of each level game, is called every 16 ms"""
        self.check_for_platform(self.player)
        self.player.move()
        for enemy in self.enemies:
            self.check_for_platform(enemy)
            enemy.move()
        self.camera.update()
        if not self.check_for_end():
            self.root.after(16, self.game)
        else:
            self.camera.end_level()
            self.end_level = True

    def start_game(self):
        self.bind_all()
        self.game()
