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
                self.canvas.create_rectangle(platform.x, 600 - platform.y,
                                             platform.x + platform.width,
                                             600 - platform.y + platform.height, fill="Green")
            )
        self.player_id = self.canvas.create_rectangle(self.player.x, self.player.y,
                                                      self.player.x + self.player.width,
                                                      self.player.y + self.player.height, fill="Red")
        self.enemies = enemies

    def update(self):
        coordinates = self.canvas.coords(self.player_id)
        self.canvas.update()
