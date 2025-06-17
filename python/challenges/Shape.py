class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        print("{}".format(self.width * self.height))

    def get_param(self):
        print("{}".format((self.width + self.height) * 2))

    def render(self):
        print("{}x{}".format(self.width, self.height))


Rect = Shape(20, 10)

Rect.render()
Rect.get_param()