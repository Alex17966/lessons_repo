import math


class Shape:
    @staticmethod
    def side_long(dot1, dot2):
        return math.sqrt((dot1[0] - dot2[0]) ** 2
                         + (dot1[1] - dot2[1]) ** 2)


class Circle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ab = self.side_long(a, b)

    def perimeter(self):
        return f'Perimeter is {round(2 * 3.14 * self.ab, 2)}'

    def area(self):
        return f'Area is {round(3.14 * self.ab ** 2, 2)}'


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = self.side_long(a, b)
        self.bc = self.side_long(b, c)
        self.ac = self.side_long(a, c)

    def perimeter(self):
        return f'Perimeter is {round(self.ab + self.bc + self.ac, 2)}'

    def area(self):
        semi_perimeter = (self.ab + self.bc + self.ac) / 2
        area = round(math.sqrt(semi_perimeter *
                               (semi_perimeter - self.ab) *
                               (semi_perimeter - self.bc) *
                               (semi_perimeter - self.ac)), 2)
        return f'Area is {area}'


class Rectangle(Shape):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = self.side_long(a, b)
        self.bc = self.side_long(b, c)

    def perimeter(self):
        return f'Perimeter is {round((self.ab + self.bc) * 2, 2)}'

    def area(self):
        return f'Area is {round(self.ab * self.bc)}'


circle = Circle((1, 1), (1, 2))
print('Circle created')
print(circle.perimeter())
print(circle.area())

triangle = Triangle((0, 0), (1, 0), (0, 1))
print('\nTriangle created')
print(triangle.perimeter())
print(triangle.area())

rectangle = Rectangle((0, 0), (0, 1), (2, 1), (2, 0))
print('\nRectangle created')
print(rectangle.perimeter())
print(rectangle.area())
