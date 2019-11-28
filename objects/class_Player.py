# class body
class Player:
    def __init__(self, canvas, x, y, height, width):
        """
        PLayer class constructor
        Args:
            canvas
            (x, y) - coordinates of the top left point of the rectangle in which the model is enclosed
            height, width - height and width of this rectangle
        """
        self.canvas = canvas
        self.live = True
        self.x = x  # It is coordinates in natural coordinate system (not canvas coordinate system)
        self.y = y
        self.height = height
        self.width = width
        self.id = self.canvas.create_rectangle(x, y, x + width, y + height, fill="Green")

    def move(self, vx, vy):
        self.x += vx
        self.y += vy
