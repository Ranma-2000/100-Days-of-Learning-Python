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
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),  # Call another class as an attribute
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

# TODO-1: Create a def that can read multi drink orders as once.
#   Problem: the output is not an object so it cannot check ingredients.
# TODO-2: Change the code to create a dict with keys is objects from Menu class to check ingredients
    def order_drink(self, *args):
        """Order as many drinks as you want. Returns items if they exist, otherwise returns None"""
        valid_item = [item.name for item in self.menu]
        order_dict = {item: 0 for item in self.menu}
        wrong_order = []
        for item in args[0]:
            if item not in valid_item:
                wrong_order.append(item)
                print("Sorry that item is not available: {}".format(item))
            for menu_item in self.menu:
                if menu_item.name == item:
                    order_dict[menu_item] = order_dict[menu_item] + 1
        return order_dict
