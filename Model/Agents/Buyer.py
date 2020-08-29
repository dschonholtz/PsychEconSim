"""
This is a buyer class that will buy objects from sellers
"""

from .BaseAgent import BaseAgent


class Buyer(BaseAgent):

    def __init__(self, price):
        BaseAgent.__init__(self, price)
        self.surplus = 0

    def choose_seller(self, list_of_sellers):
        """
        List of sellers must be a list of agents.
        """
        chosen = None
        list_of_sellers.sort(key=lambda x: x.estimated_price, reverse=True)
        for seller in list_of_sellers:
            if seller.estimated_price <= self.price and seller.sales == 0:
                seller.sell(seller.estimated_price)
                self.surplus = self.price - seller.estimated_price
                chosen = seller
                break
        return chosen
