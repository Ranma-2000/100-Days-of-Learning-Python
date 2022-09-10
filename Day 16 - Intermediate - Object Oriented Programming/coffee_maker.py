class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 3000,
            "milk": 2000,
            "coffee": 1000,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, order):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item, count in order.items():
            if count > 0:
                for ingre in item.ingredients:
                    if item.ingredients[ingre]*count > self.resources[ingre]:
                        can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item, count in order.items():
            if count > 0:
                for ingre in item.ingredients:
                    self.resources[ingre] -= item.ingredients[ingre]*count
                print(f"Here is your {item.name} ☕️. Enjoy!")

# TODO-1: Create a method that calculate the final charge for customer.
    @staticmethod
    def charge(order):
        cost = 0
        for item, count in order.items():
            if count > 0:
                cost = cost + item.cost*count
        return cost
