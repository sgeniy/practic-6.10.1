class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def get_rectangle(self):
        return self.x, self.y, self.width, self.height

fig = Rectangle(5, 10, 50, 100)

print(fig.get_rectangle())