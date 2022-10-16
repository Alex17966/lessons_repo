class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} has a salary {self.salary}, bonus {self.bonus},' \
               f' total bonus {self.calculate_total_bonus()} rub '


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)
        self.name = name


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)
        self.name = name


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)
        self.name = name


masha = Cleaner('Masha')
print(masha)
print(dir(masha))
# grisha = Manager('Grigoriy Ivanovich')
# print(grisha)
# ivan_palych = CEO('Ivan Pavlovich')
# print(ivan_palych)
print('hi')
print('hi')
print('hi')
print()
a = 10
