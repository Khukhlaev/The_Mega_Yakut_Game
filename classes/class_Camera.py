"""This class will operate with canvas coordinate system (x, y), point (0,0) on the left top side of the window
"""

from PIL import ImageTk


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
                                             platform.y + platform.height, outline="white",
                                             fill="Green")
            )
        self.player_hit_box = self.canvas.create_rectangle(self.player.x, self.player.y,
                                                           self.player.x + self.player.width,
                                                           self.player.y + self.player.height, outline="white",
                                                           fill="white")
        render = ImageTk.PhotoImage(self.player.sprite)
        self.player_id = canvas.create_image(self.player.x + self.player.width / 2, self.player.y + 2, image=render)
        self.show_sprite = render
        self.enemies = []
        for enemy in enemies:
            self.enemies.append([enemy,
                                self.canvas.create_rectangle(enemy.x, enemy.y,
                                                             enemy.x + enemy.width,
                                                             enemy.y + enemy.height, fill="Red")]
                                )
        self.enemies_id = []
        # self.enemy_sprites = []
        # for enemy in enemies:
        #     render = ImageTk.PhotoImage(enemy.sprite)
        #     self.enemy_sprites.append(render)
        #     self.enemies_id.append(
        #         canvas.create_image(enemy.x + enemy.width / 2, enemy.y, image=render))

    def player_on_center(self):
        """Return False if we need to center model of the player
                  True if we don't need this (player is already on center)
        """
        if self.canvas.coords(self.player_hit_box)[2] < self.canvas.winfo_width() / 2 or self.player.vx < 0:
            return False
        return True

    def end_level(self):
        self.canvas.create_text(self.canvas.winfo_width() - 400, 200,
                                text="Thank you Yakut!",
                                font="Arial 20", fill="red")
        self.canvas.create_text(self.canvas.winfo_width() - 400, 250,
                                text="But your president is in the another city! ",
                                font="Arial 20", fill="red")

    def update(self):
        """This method is responsible for opening a new part of the world when player reaches middle of the window"""
        canvas = self.canvas
        coordinates = self.canvas.coords(self.player_id)
        self.player.set_sprite()
        canvas.delete(self.player_id)
        render = ImageTk.PhotoImage(self.player.sprite)
        self.player_id = canvas.create_image(coordinates[0], coordinates[1], image=render)
        self.show_sprite = render
        if self.player_on_center():
            for platform in self.platforms_id:
                self.canvas.move(platform, - self.player.vx, 0)  # Move all platforms on the canvas to center player
            for enemy in self.enemies:
                self.canvas.move(enemy[1], - self.player.vx, 0)  # Move enemies hit boxes on the canvas to center player
            self.canvas.move(self.player_hit_box, 0, self.player.vy)  # Move player on the canvas y coordinate
            self.canvas.move(self.player_id, 0, self.player.vy)  # Move player on the canvas y coordinate
        else:
            self.canvas.move(self.player_hit_box, self.player.vx, self.player.vy)
            self.canvas.move(self.player_id, self.player.vx, self.player.vy)
            for enemy in self.enemies:
                self.canvas.move(enemy[1], enemy[0].vx, enemy[0].vy)  # Move enemies for their own logic
        if self.player.push_on_platform:
            self.player.push_on_platform = False
            self.player.vy = 0
        if self.player.push_under_platform:
            self.player.push_under_platform = False
            self.player.vy = 0
        if self.player.push_x:
            self.player.push_x = False
            self.player.vx = 0
        for enemy in self.enemies:
            if enemy[0].push_on_platform:
                enemy[0].push_on_platform = False
                enemy[0].vy = 0
            if enemy[0].push_under_platform:
                enemy[0].push_under_platform = False
                enemy[0].vy = 0
        self.canvas.update()
