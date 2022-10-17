import math


class Circle:
    """
    Приходят координаты(2 точки):
    а - центр, b - точка на окружности
    метод side_long вычисляет расстояние между точками(радиус)
    """

    def __init__(self, a, b):
        def side_long(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)

        self.a = a
        self.b = b
        self.ab = side_long(a, b)

    def perimeter(self):
        return round(2 * 3.14 * self.ab, 2)

    def area(self):
        return round(3.14 * self.ab ** 2, 2)


class Triangle(Circle):
    """
    ПОМОГИТЕ ПОЖАЛУЙСТА! Здесь ошибка в конструкторе
    1) Как мне правильно унаследавать класс Треугольник от класса Круг, что бы добавить точку "с" и получить длинны
    3 сторон (ab, bc, ac). У меня Пайчарм не видит метод "side_long" в классе Треугольник. Что я делаю не так?

    2) Затем я собираюсь унаследовать класс Прямоугольник от класса Круг, добавив при этом точки "с", "d" и вычислив
    длинны сторон (ab, bc, cd, ad). Это вообще правильный подход? Или нужно было создать некий абстрактный класс Shape,
    а от него наследовать 3 класса - Круг, Треугольник, Прямоугольник?
    """
    def __init__(self, a, b, c):
        super().__init__(self, c)
            self.ac = side_long(a, c)

    def perimeter(self):
        return round(self.ab + self.bc + self.ac, 2)

    def area(self):
        semi_perimeter = (self.ab + self.bc + self.ac) / 2
        return round(math.sqrt(semi_perimeter *
                         (semi_perimeter - self.ab) *
                         (semi_perimeter - self.bc) *
                         (semi_perimeter - self.ac)), 2)


circle = Circle((1, 1), (1, 2))
print(circle.perimeter())
print(circle.area())
# triangle1 = Triangle((0, 0), (1, 0), (0, 1))
# print(triangle1.perimeter())
# print(triangle1.area())
