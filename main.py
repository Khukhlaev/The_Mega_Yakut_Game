import tkinter as tk
from classes.class_Level import Level
import load_level as load

# make constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NUMBER_OF_LEVELS = 1

number_of_current_level = 1
level = ""
# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
canvas.update()


def new_game():
    global number_of_current_level, level
    parameters = load.load_level(number_of_current_level)  # Argument - number of the level
    level = Level(root, canvas, parameters[0], parameters[1], parameters[2], None)
    level.start_game()
    check_level_for_end()


def new_level():
    global number_of_current_level
    canvas.delete(tk.ALL)
    number_of_current_level += 1
    root.after(1000, new_game)


def check_level_for_end():
    global level
    if not level.end_level:
        root.after(17, check_level_for_end)
    else:
        new_level()


# start game
new_game()

root.mainloop()
