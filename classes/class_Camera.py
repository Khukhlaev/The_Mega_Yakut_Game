"""This class will operate with canvas coordinate system (x, y), point (0,0) on the left top side of the window
"""

from PIL import Image, ImageTk


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
        img = Image.open("graphics/sprites/player_static_right.png")
        self.player_hit_box = self.canvas.create_rectangle(self.player.x, self.player.y,
                                                           self.player.x + self.player.width,
                                                           self.player.y + self.player.height, outline="white",
                                                           fill="white")
        render = ImageTk.PhotoImage(img)
        self.player_id = canvas.create_image(self.player.x, self.player.y, image=render)
        self.show_sprite = render
        self.enemies = enemies
        self.level_x = 0

    def player_on_center(self):
        """Return False if we need to center model of the player
                  True if we don't need this (player is already on center)
        """
        if self.canvas.coords(self.player_hit_box)[2] < self.canvas.winfo_width() / 2 or self.player.vx < 0:
            return False
        return True

    def end_level(self):
        self.canvas.create_text(self.canvas.winfo_width() - 400, 200,
                                text="Thank you Yakut.",
                                font="Arial 20", fill="red")
        self.canvas.create_text(self.canvas.winfo_width() - 400, 300,
                                text="But your president is in another city! ",
                                font="Arial 20", fill="red")

    def update(self):
        coordinates = self.canvas.coords(self.player_hit_box)
        if self.player_on_center():
            for platform in self.platforms_id:
                self.canvas.move(platform, - self.player.vx, 0)  # Move all platforms on the canvas to center player
            self.canvas.move(self.player_hit_box, 0, self.player.vy)  # Move player on the canvas y coordinate
            self.canvas.move(self.player_id, 0, self.player.vy)  # Move player on the canvas y coordinate
            self.level_x += self.player.vx
        else:
            self.canvas.move(self.player_hit_box, self.player.vx, self.player.vy)
            self.canvas.move(self.player_id, self.player.vx, self.player.vy)
        if self.player.push_on_platform:
            self.player.push_on_platform = False
            self.player.vy = 0
        if self.player.push_under_platform:
            self.player.push_under_platform = False
            self.player.vy = 0
        self.canvas.update()
