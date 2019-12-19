import tkinter as tk
from classes.class_GameApp import GameApp

# make constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NUMBER_OF_LEVELS = 5

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.overrideredirect(1)
root.state('zoomed')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
canvas.update()

app = GameApp(NUMBER_OF_LEVELS, root, canvas)
app.main_menu()

root.mainloop()
