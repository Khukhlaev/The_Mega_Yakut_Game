# importing necessary modules
from PIL import Image, ImageTk


# class body
class Player:

    def __init__(self, canv, x, y, height, width):
        """
        Target class constructor
        """
        self.canvas = canv
        self.live = 1
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        img = Image.open("testimport.png") #TODO check if Label works or not
        render = ImageTk.PhotoImage(img)
        self.id = Label(canv, image=render)
        self.id.image = render

    def move(self, velocity):
        if velocity < 0:
            self.canvas.move(self.id, velocity, 0) #TODO check if it works with images
