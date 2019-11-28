"""This class will operate only with normal coordinate system (x, y), point (0,0) on the left bottom side of the level

"""


from objects.class_Platform import Platform


class Level:

    def __init__(self, length, camera, platforms, person, enemies):
        self.length = length  # Length of the level in coordinates units??
        self.camera = camera
        self.platforms = platforms
        self.person = person
        self.enemies = enemies
        self.end_level = False
        self.real_vx = 0
        self.real_vy = 0

    def draw_all(self, velocity):
        pass

    def change_coords(self):
        pass

    def cadre(self):
        self.change_coords()
        self.draw_all(2)

    def check_for_end(self):
        pass

    def bind_all(self):
        self.canvas.bind("<KeyPress>", self.key_interpretator)
        self.canvas.bind("<KeyRelease>", self.key_release)

    def key_interpretator(self, event):
        if event.keycode == 39:
            self.real_vx = 5
        if event.keycode == 37:
            self.real_vx = -5

    def key_release(self, event):
        self.real_vx = 0

    def game(self):
        self.bind_all()
        while not self.end_level:
            self.person.move(self.real_vx, self.real_vy)
            if self.canvas.coords(self.person.id)[0] > 380:
                pass
