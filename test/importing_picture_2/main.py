import tkinter as tk
from classes.class_Level import Level
from objects.class_Player import Player

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
level1 = Level(canvas, None, None, None)
player1 = Player(canvas, 300, 300, 100, 100)

root.mainloop()