# The maestro pizza maker is aware of the fact that the fat content of the ingredients is random and it is not always the same.
# Since fat is the most important factor in taste, the maestro pizza maker wants to know how risky his pizza menu is.
from typing import Any

import numpy as np

# TODO: define 2 risk measures for the pizza menu and implement them (1 - Taste at Risk (TaR), 2 - Conditional Taste at Risk (CTaR), also known as Expected Shorttaste (ES)

from maestro_pizza_maker.pizza import Pizza
from maestro_pizza_maker.pizza_menu import PizzaMenu


def taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    # TODO: implement the taste at risk measure for a pizza
    # quantile is the quantile that we want to consider
    # Hint: Similarity between the Taste at Risk and the Value at Risk is not a coincidence or is it?
    # Hint: Use function taste from Pizza class, but be aware that the higher the taste, the better -> the lower the taste, the worse
    # MK: Not sure whether you are referring to this: If the confidence level
    # (thinking of figures of 95% or greater) was given as a parameter,
    # q=quantile would have to be changed to q=(1 - quantile) in numpy's
    # quantile function below.
    # Considering taste in the context of pizzas is similar
    # to considering changes in value, gains, or returns of a portfolio in
    # finance: The lower the changes in value, gains, or returns, the worse.
    # Thus, we focus on the left tail of the taste distribution.
    # Since taste is always positive (due to clip(min=0.1) method in
    # _generate_multivariate_normal_vector(dim) in file fat_generator.py,
    # line 25), we omit the conventional minus sign from the definition of
    # Value at Risk, which ensures positivity.
    return np.quantile(a=pizza.taste, q=quantile).item()


def taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    # TODO: implement the taste at risk measure for a menu
    # quantile is the quantile that we want to consider
    # Hint: the taste of the whole menu is the sum of the taste of all pizzas in the menu, or? ;)
    # MK: Taste-wise, I could also imagine that the taste of the whole menu is
    # the average of the taste of all pizzas or that the taste of the whole menu
    # is even less than the taste of each pizza considered alone (thinking of e.g.
    # combining Pizza Hawaii with a pizza with sausage, tuna, and garlic. ;-)
    menu_taste: np.ndarray = sum(pizza.taste for pizza in menu.pizzas)
    return np.quantile(a=menu_taste, q=quantile).item()


def conditional_taste_at_risk_pizza(pizza: Pizza, quantile: float) -> float:
    # TODO: implement the conditional taste at risk measure for a pizza
    # quantile is the quantile that we want to consider
    # Hint: Similarity between the Conditional Taste at Risk and the Conditional Value at Risk is not a coincidence or is it?
    tar: float = taste_at_risk_pizza(pizza=pizza, quantile=quantile)
    return pizza.taste[pizza.taste <= tar].mean().item()


def conditional_taste_at_risk_menu(menu: PizzaMenu, quantile: float) -> float:
    # TODO: implement the conditional taste at risk measure for a menu
    # Hint: the taste of the whole menu is the sum of the taste of all pizzas in the menu, or? ;) (same as for the taste at risk)
    menu_taste: np.ndarray = sum(pizza.taste for pizza in menu.pizzas)
    tar: float = np.quantile(a=menu_taste, q=quantile).item()
    return menu_taste[menu_taste <= tar].mean().item()
