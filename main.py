import tkinter as tk
import sys
sys.path.append('/objects') #TODO fix
from class_Player import Player

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
k = Player
