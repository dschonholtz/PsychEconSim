from .BaseAgent import BaseAgent


class Seller(BaseAgent):

    def __init__(self, price):
        BaseAgent.__init__(self, price)
        self.sales = 0
        self.profit = 0
        self.historical_prices = []
        self.estimated_price = self.price + .25

    def sell(self, price):
        self.sales += 1
        self.profit += price - self.price

    def adjust_estimated_price(self):
        temp_sales = self.sales
        temp_est_price = self.estimated_price
        self.historical_prices.append((temp_est_price, temp_sales),)
        if len(self.historical_prices) > 9:
            self.historical_prices.pop()
        if self.sales:
            safe_to_raise_prices = True
            for hp in self.historical_prices:
                if hp[0] <= self.estimated_price + .25 and hp[1] == 0:
                    safe_to_raise_prices = False
            if safe_to_raise_prices:
                self.estimated_price += .25
        elif self.estimated_price - .25 >= self.price:
            self.estimated_price -= .25
        self.sales = 0
        self.profit = 0
