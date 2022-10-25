class Human:
    default_name = None
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'name: {self.name},\nage: {self.age},\nmoney: {self.__money},\nhouse: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name is {Human.default_name}, default age is {Human.default_age}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        # print(f'House with {house_price} is bought')

    def earn_money(self, money_amount):
        self.__money += money_amount
        print(f'You earned {money_amount}, you have {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enough money')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'final_price is: {final_price}')
        return final_price


class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


Human.default_info()
alexander = Human('Sasha', 27)
alexander.info()
small_house = SmallHouse(8500)
alexander.buy_house(small_house, 5)
alexander.earn_money(5000)
alexander.buy_house(small_house, 5)

alexander.earn_money(20000)
alexander.buy_house(small_house, 5)
alexander.info()





