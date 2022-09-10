from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.order_drink(choice.split(','))
        cost = CoffeeMaker.charge(order)

        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(cost):
            coffee_maker.make_coffee(order)
