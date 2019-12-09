import tkinter as tk
from classes.class_Level import Level
import load_level as load

# make constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
canvas.update()

parameters = load.load_level(1)  # Argument - number of the level

level1 = Level(root, canvas, 1000, parameters[0], parameters[1], None)

level1.start_game()

root.mainloop()
