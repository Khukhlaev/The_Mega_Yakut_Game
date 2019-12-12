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

    def check_for_platform(self):
        on_platform = False
        for platform in self.platforms:
            # check for platform below
            if (platform.y + platform.height / 2 >= self.player.y + self.player.height + self.player.vy >=
                platform.y) \
                    and ((platform.x + platform.width >= self.player.x + self.player.vx >= platform.x) or
                         (
                                 platform.x + platform.width >= self.player.x + self.player.width + self.player.vx >=
                                 platform.x)) and self.player.vy >= 0:
                on_platform = True
                self.push_up(platform)
                break
            # check for platform ahead
            if (platform.y + platform.height / 2 < self.player.y + self.player.vy <
                platform.y + platform.height) \
                    and ((platform.x + platform.width >= self.player.x + self.player.vx >= platform.x) or
                         (
                                 platform.x + platform.width >= self.player.x + self.player.width + self.player.vx >=
                                 platform.x)) and self.player.vy <= 0:
                self.push_down(platform)
                break
            # check for platform on the left
            if (platform.x + platform.width > self.player.x + self.player.vx > platform.x + platform.width / 2) and \
                    (
                            platform.y + platform.height > self.player.y > platform.y or
                            platform.y + platform.height > self.player.y + self.player.height > platform.y):
                self.player.vx = (platform.x + platform.width) - self.player.x
                break
            # check for platform on the right
            if (platform.x + platform.width / 2 > self.player.x + self.player.width + self.player.vx > platform.x) and \
                    (
                            platform.y + platform.height > self.player.y > platform.y or
                            platform.y + platform.height > self.player.y + self.player.height > platform.y):
                self.player.vx = (self.player.x + self.player.width) - platform.x
                break
        self.player.on_platform = on_platform

    def push_up(self, platform):
        """This method is for preventing some bugs and push player straightly onto the platform"""
        if self.player.vy != 0:
            self.player.vy = platform.y - (self.player.y + self.player.height)
            self.player.push_on_platform = True

    def push_down(self, platform):
        """This method is for preventing some bugs and push player down when he touch platform ahead"""
        if self.player.vy != 0:
            self.player.vy = (platform.y + platform.height) - self.player.y
            self.player.push_under_platform = True

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
        self.check_for_platform()
        self.player.move()
        self.camera.update()
        if not self.check_for_end():
            self.root.after(16, self.game)
        else:
            self.camera.end_level()
            self.end_level = True

    def start_game(self):
        self.bind_all()
        self.game()
