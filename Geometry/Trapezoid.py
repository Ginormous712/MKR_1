from Quadrangle import Quadrangle

import math


class Trapeoid(Quadrangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.__height = self.calculate_height()

    @property
    def height(self):
        return self.__height

    # Separating the trapezoid into two rectangles
    # Looking for the intersection point of lines passing through opposite vertices
    def calculate_height(self):
        x1, y1 = self.vertices[0]
        x2, y2 = self.vertices[1]
        x3, y3 = self.vertices[2]
        x4, y4 = self.vertices[3]

        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)

        x_intersect = (m1 * x1 - y1 - m2 * x3 + y3) / (m1 - m2)
        y_intersect = m1 * (x_intersect - x1) + y1

        height = abs(y_intersect - y2)
        return height

    def calculate_area(self):
        return (self.sides[1] + self.sides[3]) / 2 * self.height

    # Checking adjacent angles
    def check_properties(self):
        return math.isclose(self.angles[0] + self.angles[1], self.angles[2] + self.angles[3])

    def __str__(self):
        print("Trapezoid with vertices: ", self.vertices)

