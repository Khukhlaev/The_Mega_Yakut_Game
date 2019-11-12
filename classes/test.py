import tkinter as tk
from random import randrange as rnd
from class_platform import Platform
from class_Person import Person

# make window
root = tk.Tk()
root.title('The Mega Yakut Game')
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

person = Person(canv, 100, 80, 20, 10)
platforms = [Platform(canv, 100, 100, 100, 20)]
velocity = 0
k = 0


def key_interpretator(event):
    global velocity
    if event.keycode == 39:
        velocity = 5
    if event.keycode == 37:
        velocity = -5


def key_release(event):
    global velocity
    velocity = 0


root.bind("<KeyPress>", key_interpretator)
root.bind("<KeyRelease>", key_release)


def game():
    global platforms, velocity, k, person
    k += 1
    if k % 50 == 0 and velocity > 0:
        platforms += [Platform(canv, 400, 100, 100, 20)]
    for p in platforms:
        p.move(velocity)
    person.move(velocity)
    root.after(30, game)


game()
# def game():
root.mainloop()
