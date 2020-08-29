"""
Base Agent class that other agents inherit from
"""
import numpy as np


class BaseAgent:
    """
    BaseAgent class that is used by other agent classees
    """

    def __init__(self, price):
        """
            Constructor
        """
        self.price = self.get_normal_price(price)

    @staticmethod
    def get_normal_price(price):
        return np.random.normal(price)

