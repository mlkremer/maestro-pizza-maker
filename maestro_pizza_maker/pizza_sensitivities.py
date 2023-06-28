# The maestro pizza maker wants to fully understand of the properties of his pizza menu.
# Therefore he defines the following variables in the pizza industry known as "pizza sensitivities":
# 1. menu_sensitivity_protein - represents the rate of change between the price of the pizza and the amount of protein in the pizza
# 2. menu_sensitivity_carbs - represents the rate of change between the price of the pizza and the amount of carbohydrates in the pizza
# 3. menu_sensitivity_fat - represents the rate of change between the price of the pizza and the amount of average_fat in the pizza

# TODO: implement above mentioned sensitivities
# hint: simple linear regression might be helpful

import numpy as np
from sklearn.linear_model import LinearRegression

from maestro_pizza_maker.pizza_menu import PizzaMenu


def menu_sensitivity_protein(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    x = np.reshape([pizza.protein for pizza in menu.pizzas], (-1, 1))
    y = np.array([pizza.price for pizza in menu.pizzas])
    reg = LinearRegression()
    reg.fit(x, y)
    return reg.coef_.item()


def menu_sensitivity_carbs(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    x = np.reshape([pizza.carbohydrates for pizza in menu.pizzas], (-1, 1))
    y = np.array([pizza.price for pizza in menu.pizzas])
    reg = LinearRegression()
    reg.fit(x, y)
    return reg.coef_.item()


def menu_sensitivity_fat(menu: PizzaMenu) -> float:
    # TODO: implement according to the description above
    x = np.reshape([pizza.average_fat for pizza in menu.pizzas], (-1, 1))
    y = np.array([pizza.price for pizza in menu.pizzas])
    reg = LinearRegression()
    reg.fit(x, y)
    return reg.coef_.item()
