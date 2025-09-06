import utils
# Test the utils functions
print(f"{utils.convert(500000)} m^2")
print(f"The larger area between is {utils.larger_shape_area(50, 30)} m^2")
print(f"The larger area is {utils.larger_shape_area(20, 70)} m^2")

from shape import circle, rectangle, triangle
rect_1=rectangle(4,5)
rect_1.describe()
tri_1=triangle(3,6)
tri_1.describe()
circle_1=circle(10)
circle_1.describe()
