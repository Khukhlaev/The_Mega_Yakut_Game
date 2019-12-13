"""This class is responsible for move from one level to new one and start it"""

from classes.class_Level import Level
import load_level as load
from tkinter import ALL


class GameApp:

    def __init__(self, number_of_levels, root, canvas):
        self.number_of_levels = number_of_levels
        self.root = root
        self.canvas = canvas
        self.number_of_current_level = 1
        self.current_level = ''

    def new_level_game(self):
        """This method will start new level"""
        self.canvas.delete(ALL)
        parameters = load.load_level(self.number_of_current_level)  # Argument - number of the level
        self.current_level = Level(self.root, self.canvas, parameters[0], parameters[1], parameters[2], parameters[3])
        self.start_game()

    def bind_all(self):
        self.root.bind("<KeyPress>", self.key_interpreter)
        self.root.bind("<KeyRelease>", self.key_release)

    def key_interpreter(self, event):
        if event.keycode == 39:
            self.current_level.player.move_right()
        if event.keycode == 37:
            self.current_level.player.move_left()
        if event.keycode == 38 and self.current_level.player.on_platform:
            self.current_level.player.jump()

    def key_release(self, event):
        if event.keycode == 39 or event.keycode == 37:
            self.current_level.player.vx = 0

    def game_tic(self):
        self.current_level.game()
        player_live = self.current_level.check_for_live()
        if not self.current_level.end_level and player_live:
            self.root.after(16, self.game_tic)
        elif self.current_level.end_level:
            self.new_level()
        else:
            self.new_level_game()

    def start_game(self):
        self.bind_all()
        self.game_tic()

    def new_level(self):
        """This method will increase number of current level if player finish previous one"""
        if self.number_of_current_level < self.number_of_levels:
            self.number_of_current_level += 1
        self.root.after(10000, self.new_level_game)
