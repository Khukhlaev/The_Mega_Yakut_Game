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
        self.current_level.start_game()
        self.check_level_for_end()

    def new_level(self):
        """This method will increase number of current level if player finish previous one"""
        if self.number_of_current_level < self.number_of_levels:
            self.number_of_current_level += 1
        self.root.after(10000, self.new_level_game)

    def check_level_for_end(self):
        """This method will check level for end, is called every 100 ms"""
        if not self.current_level.end_level:
            self.root.after(100, self.check_level_for_end)
        else:
            self.new_level()

    def check_for_death(self):
        """This method checks if player is alive"""
        if not self.current_level.player.live:
            self.new_level_game()
        else:
            self.root.after(100, self.check_for_death)

