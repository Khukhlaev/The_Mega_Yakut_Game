# importing necessary modules


# class body
class Platform:

    def __init__(self, canv, x, y, length, width):
        """
        Target class constructor
        """
        self.canvas = canv
        self.live = 1
        self.x = x
        self.y = y
        self.height = length
        self.width = width
        self.id = self.canvas.create_rectangle(x, y, x + length, y + width, fill="Green")

    def move(self, velocity):
        self.canvas.move(self.id, -velocity, 0)
