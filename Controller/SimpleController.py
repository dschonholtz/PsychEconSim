"""
The simplest of controllers. Uses a base market and a TextView
"""


class SimpleController:

    def __init__(self, text_view, simple_market, rounds=30):
        self.view = text_view
        self.model = simple_market
        self.successful_sellers = 0
        self.successful_buyers = 0
        self.average_buyer_surplus = 0
        self.average_seller_profit = 0
        self.rounds = rounds

    def start(self):
        self.run_market()

    def run_market(self):
        for i in range(self.rounds):
            self.reset_market_except_seller_prices()
            print("On round {0} of {1}".format(i + 1, self.rounds))
            sellers = self.model.sellers
            total_buyer_surplus = 0
            total_seller_profit = 0
            for buyer in self.model.buyers:
                chosen_seller = buyer.choose_seller(sellers)
                if chosen_seller is not None:
                    total_buyer_surplus += buyer.price - chosen_seller.estimated_price
                    total_seller_profit += chosen_seller.estimated_price - chosen_seller.price
                    self.successful_sellers += 1
                    self.successful_buyers += 1
            self.average_buyer_surplus = total_buyer_surplus / self.successful_buyers
            self.average_seller_profit = total_seller_profit / self.successful_sellers
            self.view.show_stats(self.successful_sellers, self.successful_buyers, self.average_seller_profit,
                                 self.average_buyer_surplus)
            new_sellers = []
            for seller in self.model.sellers:
                seller.adjust_estimated_price()
                new_sellers.append(seller)
            self.model.sellers = new_sellers

    def reset_market_except_seller_prices(self):
        self.successful_buyers = 0
        self.successful_sellers = 0
        self.average_buyer_surplus = 0
        self.average_seller_profit = 0
