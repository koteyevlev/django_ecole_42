#!/usr/bin/env python3
from beverages import *
import random


class CoffeeMachine:
    def __init__(self):
        self.is_working = True
        self.num_of_usage = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = "empty cup"
            self.price = 0.9

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, msg="This coffee machine has to be repaired."):
            Exception.__init__(self, msg)

    def repair(self):
        self.is_working = True
        self.num_of_usage = 0

    def serve(self, some_beverage):
        self.num_of_usage += 1
        if self.num_of_usage > 10:
            self.is_working = False
        if not self.is_working:
            raise self.BrokenMachineException()
        return some_beverage() if random.randint(0, 1) == 0 else self.EmptyCup()


def machine():
    """
    test
    :return:
    """
    coffee_machine = CoffeeMachine()
    for _ in range(2):
        try:
            for i in range(13):
                print(i, coffee_machine.serve(random.sample(
                    [Coffee, HotBeverage, Chocolate, HotBeverage, Tea], 1)[0]))
        except Exception as e:
            print(e)
            coffee_machine.repair()
            print("\nRepaired\n")


if __name__ == "__main__":
    machine()
