import numpy as np


class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

    def order_drink(self, *args):
        """Order as many drinks as you want. Returns items if they exist, otherwise returns None"""
        item_dict = {item.name: 0 for item in self.menu}
        wrong_order = []
        for arg in args:
            if type(arg) == list:
                for item in arg:
                    if item in item_dict.keys():
                        item_dict[item] = item_dict[item] + 1
                    else:
                        wrong_order.append(item)
                        print(f'Sorry we don\'t have {item}')
            else:
                if arg in item_dict.keys():
                    item_dict[arg] = item_dict[arg] + 1
                else:
                    wrong_order.append(arg)
                    print(f'Sorry we don\'t have {arg}')
        return item_dict
