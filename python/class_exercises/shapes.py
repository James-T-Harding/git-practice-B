from abc import ABC, abstractmethod
from math import sqrt, ceil


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
    VERT = "|"
    HOR = "-"
    SPACE = " "

    def __str__(self):
        s_list = [self.horizontal_side]

        for _ in range(ceil(self.height/2)):
            s_list.append(self.VERT + self.gaps * self.SPACE + self.VERT)

        s_list.append(self.horizontal_side)

        return "\n".join(s_list)

    def __int__(self):
        return self.area()

    @property
    def gaps(self):
        return ceil(2.5 * self.width - 1)

    @property
    def horizontal_side(self):
        return "+" + self.gaps * self.HOR + "+"

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


if __name__ == "__main__":
    print(Rectangle(3, 3))
    print(Rectangle(3, 4))
    print(Rectangle(1, 2))
    print(Rectangle(1, 1))