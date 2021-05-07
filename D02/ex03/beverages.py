#!/usr/bin/env python3


class HotBeverage:
    def __init__(self):
        self.price = 0.3
        self.name = "hot beverage"

    def __str__(self):
        return "name : " + self.name + \
               "\nprice : " + format(self.price, ".2f") + \
               "\ndescription : " + self.description()

    def description(self):
        return "Just some hot water in a cup."


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.4

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate"
        self.price = 0.5

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


