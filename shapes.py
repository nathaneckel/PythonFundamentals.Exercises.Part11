class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


if __name__ == "__main__":
    rect = Rectangle(2, 4)
    print(rect.area())

    square = Square(8)
    print(square.area())
    print(square.perimeter())

