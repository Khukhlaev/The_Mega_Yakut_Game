import tkinter as tk
from classes.class_Level import Level
import load_level as load

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)


parameters = load.load_level()

level1 = Level(root, canvas, 1000, parameters[0], parameters[1], None)

level1.game()


root.mainloop()