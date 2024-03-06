#!/usr/bin/env python3

class HotBeverage:
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot beverage"
        self._description = "Just some hot water in a cup."

    def description(self) -> str:
        return self._description
    
    def __str__(self) -> str:
        return "name : " + self.name + "\nprice : " + "{:.2f}".format(self.price) + "\ndescription : " + self.description()


class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.40
        self.name = "coffee"
        self._description = "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'tea'

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.name = 'chocolate'
        self.price = 0.50
        self._description = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.name = "cappuccino"
        self.price = 0.45
        self._description = "Un po' di Italia nella sua tazza!"

def main():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())

if __name__ == "__main__":
    main()

