from PIL import ImageDraw

class Shape:
    def render(self, draw):
        raise NotImplementedError("Subclasses must implement render method.")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def render(self, draw):
        draw.ellipse(
            [
                self.x - self.radius, self.y - self.radius,
                self.x + self.radius, self.y + self.radius
            ],
            outline="black"
        )

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def render(self, draw):
        draw.rectangle(
            [
                self.x, self.y,
                self.x + self.side, self.y + self.side
            ],
            outline="black"
        )

class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def render(self, draw):
        draw.line(
            [
                (self.x1, self.y1),
                (self.x2, self.y2)
            ],
            fill="black"
        )
