import tkinter as tk
from classes.class_GameApp import GameApp

# make constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
NUMBER_OF_LEVELS = 2

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
canvas.update()

app = GameApp(NUMBER_OF_LEVELS, root, canvas)


def new_game():
    button_new_game.destroy()
    button_exit.destroy()
    app.new_level_game()


button_new_game = tk.Button(root, text="New game", width=15, height=3, command=new_game)
button_new_game.pack()
button_exit = tk.Button(root, text="Exit", width=15, height=3, command='')
button_exit.pack()

root.mainloop()
