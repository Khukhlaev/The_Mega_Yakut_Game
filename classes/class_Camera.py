"""This class will operate only with canvas coordinate system (x, y), point (0,0) on the left top side of the window
"""


class Camera:
    def __init__(self, canvas, player, platforms, enemies):
        """
        Camera class constructor
        Args:
            canvas
        """
        self.canvas = canvas
        self.player = player
        self.platforms_id = []
        for platform in platforms:
            self.platforms_id.append(
                self.canvas.create_rectangle(platform.x, platform.y,
                                             platform.x + platform.width,
                                             platform.y + platform.height, fill="Green")
            )
        self.player_id = self.canvas.create_rectangle(self.player.x, self.player.y,
                                                      self.player.x + self.player.width,
                                                      self.player.y + self.player.height, fill="Red")
        self.enemies = enemies
        self.level_x = 0

    def player_on_center(self):
        """Return False if we need to center model of the player
                  True if we don't need this (player is already on center)
        """
        if self.canvas.coords(self.player_id)[2] < self.canvas.winfo_width() / 2 or self.player.vx < 0:
            return False
        return True

    def update(self):
        coordinates = self.canvas.coords(self.player_id)
        if self.player_on_center():
            for platform in self.platforms_id:
                self.canvas.move(platform, - self.player.vx, 0)  # Move all platforms on the canvas to center player
            self.canvas.move(self.player_id, 0, self.player.vy)  # Move player on the canvas y coordinate
            self.level_x += self.player.vx
        else:
            self.canvas.move(self.player_id, self.player.vx, self.player.vy)
        if self.player.push_on_platform:
            self.player.push_on_platform = False
            self.player.vy = 0
        self.canvas.update()

