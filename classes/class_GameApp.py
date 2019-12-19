"""This class is responsible for move from one level to new one and start it"""

from classes.class_Level import Level
import load_level as load
from tkinter import ALL, Button, CENTER
from sys import platform
from time import perf_counter, time


class GameApp:

    def __init__(self, number_of_levels, root, canvas):
        self.number_of_levels = number_of_levels
        self.root = root
        root.protocol("WM_DELETE_WINDOW", self.save_exit)  # To save current player time even if he close window
        self.canvas = canvas
        self.number_of_current_level = 1
        self.current_level = ''
        self.pause_status = False
        self.button_resume = ''
        self.button_exit = ''
        self.button_new_game = ''
        self.button_load_game = ''
        self.gaming_time = 0
        if platform == "win32" or platform == "cygwin":
            self.key_left = 37
            self.key_right = 39
            self.key_up = 38
            self.key_space = 32
        elif platform == "linux" or platform == "linux2" or platform == "linux3":
            self.key_left = 113
            self.key_right = 114
            self.key_up = 111
            self.key_space = 65
        elif platform == "darwin":
            self.key_left = 8124162
            self.key_right = 8189699
            self.key_up = 8320768
            self.key_space = 32

    def new_level_game(self):
        """This method will start new level"""
        self.canvas.delete(ALL)
        parameters = load.load_level(self.number_of_current_level)  # Argument - number of the level
        self.current_level = Level(self.canvas, parameters[0], parameters[1],
                                   parameters[2], parameters[3], parameters[4])
        self.bind_all()
        self.game_tic()

    def bind_all(self):
        self.root.bind("<KeyPress>", self.key_interpreter)
        self.root.bind("<KeyRelease>", self.key_release)

    def key_interpreter(self, event):
        if not self.pause_status:
            if event.keycode == self.key_right:
                self.current_level.player.move_right()
            if event.keycode == self.key_left:
                self.current_level.player.move_left()
            if event.keycode == self.key_up and self.current_level.player.on_platform:
                self.current_level.player.jump()
        if event.keycode == self.key_space:
            self.pause()

    def key_release(self, event):
        if event.keycode == 39 or event.keycode == 37:
            self.current_level.player.vx = 0

    def game_tic(self):
        """This is main method of each game"""
        time1 = perf_counter()  # Time before game iteration (before all logical operations)
        if not self.pause_status:
            self.current_level.game()
        player_live = self.current_level.check_for_live()
        time2 = perf_counter()  # Time after game iteration (after all logical operations)
        iteration_time = int(24 - (time2 - time1) * 1000)  # This iteration time
        if not self.current_level.end_level and player_live:
            self.root.after(iteration_time, self.game_tic)
        elif self.current_level.end_level:
            self.new_level()
        else:
            self.new_level_game()

    def new_level(self):
        """This method will increase number of current level if player finish previous one"""
        if self.number_of_current_level < self.number_of_levels:
            self.number_of_current_level += 1
            self.save_progress()
            self.gaming_time = time()
            self.canvas.create_text(self.canvas.winfo_width() - 400, 200,
                                    text="Thank you Yakut!",
                                    font="Arial 20", fill="red", justify=CENTER)
            self.canvas.create_text(self.canvas.winfo_width() - 400, 250,
                                    text="But your president is in the another city! ",
                                    font="Arial 20", fill="red", justify=CENTER)
            self.root.after(8000, self.new_level_game)
        else:
            self.game_over()

    def save_progress(self):
        save_file = open("saves/save.txt", 'r+')
        current_time = float(save_file.read().splitlines()[1])
        save_file.close()
        save_file = open("saves/save.txt", 'w')
        save_file.write(str(self.number_of_current_level) + "\n")
        save_file.write(str(time() - self.gaming_time + current_time))
        save_file.close()
        self.gaming_time = time()

    def load_game(self):
        self.button_new_game.destroy()
        self.button_load_game.destroy()
        self.button_exit.destroy()
        save_file = open("saves/save.txt", 'r+')
        self.number_of_current_level = int(save_file.readline())
        save_file.close()
        self.gaming_time = time()
        self.new_level_game()

    def save_exit(self):
        self.save_progress()
        self.root.destroy()

    def pause(self):
        if not self.pause_status:
            self.pause_status = True
            self.button_resume = Button(self.canvas, text="Resume", width=15, height=3, command=self.pause)
            self.button_resume.pack()
            self.button_exit = Button(self.canvas, text="Save and exit", width=15, height=3, command=self.save_exit)
            self.button_exit.pack()
        else:
            self.pause_status = False
            self.button_resume.destroy()
            self.button_exit.destroy()

    def new_game(self):
        self.button_new_game.destroy()
        self.button_load_game.destroy()
        self.button_exit.destroy()
        save_file = open("saves/save.txt", 'w')
        save_file.write("1\n")
        save_file.write("0")
        save_file.close()
        self.gaming_time = time()
        self.new_level_game()

    def main_menu(self):
        self.canvas.delete(ALL)
        self.button_new_game = Button(self.canvas, text="New game", width=15, height=3, command=self.new_game)
        self.button_new_game.pack()
        self.button_load_game = Button(self.canvas, text="Continue game", width=15, height=3, command=self.load_game)
        self.button_load_game.pack()
        self.button_exit = Button(self.canvas, text="Exit", width=15, height=3, command=self.save_exit)
        self.button_exit.pack()

    def game_over(self):
        self.save_progress()
        save_file = open("saves/save.txt", 'r+')
        game_time = round(float(save_file.read().splitlines()[1]), 4)
        save_file.close()
        self.canvas.create_text(self.canvas.winfo_width() - 400, 150,
                                text="Thank you Yakut!",
                                font="Arial 20", fill="red", justify=CENTER)
        self.canvas.create_text(self.canvas.winfo_width() - 400, 200,
                                text=("You've done it in " + str(game_time) + " seconds, well done!"),
                                font="Arial 20", fill="red", justify=CENTER)
        self.canvas.create_text(self.canvas.winfo_width() - 400, 250,
                                text="Thank you for playing, we hope you enjoy this experience!",
                                font="Arial 20", fill="red", justify=CENTER)
        self.canvas.create_text(self.canvas.winfo_width() - 400, 300,
                                text="Our team: Svyatoslav Khukhlaev, Alex Legoshin",
                                font="Arial 20", fill="red", justify=CENTER)
        self.canvas.create_text(self.canvas.winfo_width() - 400, 350,
                                text="and Mikhail Yaushev",
                                font="Arial 20", fill="red", justify=CENTER)
        self.canvas.create_text(self.canvas.winfo_width() - 400, 400,
                                text="Wish you the best for the future!",
                                font="Arial 20", fill="red", justify=CENTER)
        self.root.after(10000, self.main_menu)

