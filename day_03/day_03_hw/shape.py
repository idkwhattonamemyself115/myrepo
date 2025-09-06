class circle:
    def __init__(self, radius: int):
        self.radius = radius
    def area_of_circle(self):
        return 3.14159 * self.radius**2
    def describe(self):
        print(f"This circle has a radius of {self.radius} and has a area of {self.area_of_circle()}.")
class rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    def area_rectangle(self):
        return self.width * self.height
    def describe(self):
        print(f"Rectangle {self.width} by {self.height} has an area of {self.area_rectangle()}.")
class triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
    def area_triangle(self):
        return 0.5 * self.base * self.height
    def describe(self):
        print(f"This triangle has a base of {self.base} and a height of {self.height} and has an area of {self.area_triangle()}.")
circle_1=circle(7)
circle_1.describe()
rect_1=rectangle(5,10)
rect_1.describe()
tri_1=triangle(6,3)
tri_1.describe()
