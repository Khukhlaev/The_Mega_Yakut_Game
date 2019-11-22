import tkinter as tk
from classes.class_Level import Level

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
level1 = Level(canv, None, None)
