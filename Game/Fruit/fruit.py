class Fruit:
    def __init__(self, coords, pygm_obj, scr, col=(255, 0, 0), cl_sz=15, sprt='later', sou='later'):
        self.x = coords[0]
        self.y = coords[1]
        self.color = col
        self.size = cl_sz
        self.sprite = sprt
        self.sound = sou
        self.pygame_object = pygm_obj
        self.screen = scr

    def spawn(self):
        self.color = (255, 0, 0)
        self.pygame_object.draw.rect(self.screen, self.color, self.pygame_object.Rect(30, 30, 60, 60))