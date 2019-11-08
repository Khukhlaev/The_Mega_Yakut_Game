# import sys
import tkinter as tk

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


def exit_from_game():
    # sys.exit()
    pass


def new_game():
    pass


# make main menu
button_new_game = tk.Button(canv, text="New game", width=15, height=3, command=new_game)
button_new_game.pack()
button_exit = tk.Button(canv, text="Exit", width=15, height=3, command=exit_from_game)
button_exit.pack()
print("hww")

root.mainloop()