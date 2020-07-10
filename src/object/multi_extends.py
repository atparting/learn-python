class Animal:

    __name = ""

    def __init__(self, name):
        self.__name = name

    def speak(self):
        print(self.__name, "speak: ~~~")

    def name(self):
        return "Animal: " + self.__name


class Food:
    __name = ""
    __price = 0

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def name(self):
        return "Food: " + self.__name

    def price(self):
        return self.__price


class Pig(Animal, Food):

    def __init__(self):
        Animal.__init__(self, "Pig")
        Food.__init__(self, "Pig", 100)

    def speak(self):
        print("Pig speak: HengHeng")


pig = Pig()
print("name is", pig.name())
pig.speak()
print("price is", pig.price())
