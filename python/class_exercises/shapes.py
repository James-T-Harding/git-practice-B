from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class IsoscelesTriangle(Shape):
    def area(self):
        return 0.5 * self.height * self.width

    def perimeter(self):
        side_width = sqrt(self.height**2 + (self.width/2)**2)

        return self.width + 2 * side_width


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side_width):
        height = sqrt(side_width**2 - (side_width/2)**2)
        super().__init__(height, side_width)

    def perimeter(self):
        return 3 * self.width
