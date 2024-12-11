class Shape:
    def __init__(self, color="black", fill=None):
        self.color = color
        self.fill = fill

    def render(self, draw):
        raise NotImplementedError("Subclasses must implement render method.")

class Circle(Shape):
    def __init__(self, x, y, radius, color="black", fill=None):
        super().__init__(color, fill)
        self.x = x
        self.y = y
        self.radius = radius

    def render(self, draw):
        bounds = [
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius
        ]
        if self.fill:
            draw.ellipse(bounds, outline=self.color, fill=self.color)
        else:
            draw.ellipse(bounds, outline=self.color, fill=None)

class Square(Shape):
    def __init__(self, x, y, side, color="black", fill=None):
        super().__init__(color, fill)
        self.x = x
        self.y = y
        self.side = side

    def render(self, draw):
        bounds = [
            self.x, self.y,
            self.x + self.side, self.y + self.side
        ]
        if self.fill:
            draw.rectangle(bounds, outline=self.color, fill=self.color)
        else:
            draw.rectangle(bounds, outline=self.color, fill=None)

class Line(Shape):
    def __init__(self, x1, y1, x2, y2, color="black"):
        super().__init__(color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def render(self, draw):
        draw.line([(self.x1, self.y1), (self.x2, self.y2)], fill=self.color)
