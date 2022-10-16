import math


class Triangle:
    def __init__(self, a, b, c=None, d=None):
        def side_long(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = side_long(a, b)
        self.bc = side_long(b, c)
        self.ac = side_long(a, c)

    def perimeter(self):
        return round(self.ab + self.bc + self.ac, 2)

    def area(self):
        semi_perimeter = (self.ab + self.bc + self.ac) / 2
        return round(math.sqrt(semi_perimeter *
                         (semi_perimeter - self.ab) *
                         (semi_perimeter - self.bc) *
                         (semi_perimeter - self.ac)), 2)




triangle1 = Triangle((0, 0), (1, 0), (0, 1))
print(triangle1.perimeter())
print(triangle1.area())
