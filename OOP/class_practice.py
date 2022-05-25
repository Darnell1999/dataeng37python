class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.interior_angles = 360
        self.sides = 4

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter


a = Rectangle(5, 7)
area = a.get_area()
print(area)


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, height=width)
        self.width = width
        self.height = width


b = Square(4)
area = b.get_area()

perimeter = b.get_perimeter()

print(area)
print(perimeter)


