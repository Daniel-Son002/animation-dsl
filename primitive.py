from z3 import Real, Solver

class Shape:
    def __init__(self, x, y):
        self.x = Real('x')
        self.y = Real('y')
        self.solver = Solver()
        self.solver.add(self.x == x, self.y == y)

    def render(self, draw):
        raise NotImplementedError("Render method must be implemented by subclasses.")

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = Real('radius')
        self.solver.add(self.radius == radius)

    def render(self, draw):
        if self.solver.check():
            x_val = self.solver.model()[self.x].as_decimal(5)
            y_val = self.solver.model()[self.y].as_decimal(5)
            radius_val = self.solver.model()[self.radius].as_decimal(5)
            draw.ellipse(
                [
                    float(x_val) - float(radius_val),
                    float(y_val) - float(radius_val),
                    float(x_val) + float(radius_val),
                    float(y_val) + float(radius_val),
                ],
                outline="black"
            )

class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = Real('side')
        self.solver.add(self.side == side)

    def render(self, draw):
        if self.solver.check():
            x_val = self.solver.model()[self.x].as_decimal(5)
            y_val = self.solver.model()[self.y].as_decimal(5)
            side_val = self.solver.model()[self.side].as_decimal(5)
            draw.rectangle(
                [
                    float(x_val),
                    float(y_val),
                    float(x_val) + float(side_val),
                    float(y_val) + float(side_val),
                ],
                outline="black"
            )



class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def render(self, draw):
        if self.solver.check():
            x1_val = self.solver.model()[self.x1].as_decimal(5)
            y1_val = self.solver.model()[self.y1].as_decimal(5)
            x2_val = self.solver.model()[self.x2].as_decimal(5)
            y2_val = self.solver.model()[self.y2].as_decimal(5)
            draw.line([float(x1_val), float(y1_val), float(x2_val), float(y2_val)], fill="black")



class Constraint:
    def __init__(self, shape1, property1, shape2, property2):
        self.shape1 = shape1
        self.property1 = property1
        self.shape2 = shape2
        self.property2 = property2
        self.solver = Solver()
        self.solver.add(getattr(shape1, property1) == getattr(shape2, property2))

    def apply(self):
        if self.solver.check() == 'sat':
            print("Constraint applied successfully")
        else:
            print("Constraint not satisfiable")

