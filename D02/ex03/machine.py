import random
from beverages import *

class CoffeeMachine:
    def __init__(self) -> None:
        self.drinks_served = 0
    
    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self.name = "empty cup"
            self.price = 0.90
            self._description = "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")
    
    def repair(self) -> None:
        self.drinks_served = 0
        print("Machine repaired. It can now serve hot drinks again.")
    
    def serve(self, beverage:HotBeverage) -> HotBeverage:
        if self.drinks_served >= 10:
            raise self.BrokenMachineException()
        self.drinks_served += 1
        if random.randint(0, 1):
            return beverage
        return self.EmptyCup()

def main():
    machine = CoffeeMachine()
    for _ in range(25):
        try:
            random_beverage = random.choice([Tea(), Chocolate(), Cappuccino(), Coffee()])
            machine.serve(random_beverage)
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            machine.repair()
            random_beverage = random.choice([Tea(), Chocolate(), Cappuccino(), Coffee()])
            print(machine.serve(random_beverage))

if __name__ == "__main__":
    main()