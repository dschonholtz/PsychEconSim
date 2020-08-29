"""
A class design to handle the bear necessities for oa market that all other markets must have
"""
from Model.Agents.Seller import Seller
from Model.Agents.Buyer import Buyer


class BaseMarket:

    def __init__(self, num_buyers, num_sellers, buy_max_price, sell_min_price):
        buyer_list = []
        seller_list = []
        for i in range(num_buyers - 1):
            buyer = Buyer(buy_max_price)
            buyer_list.append(buyer)
        for i in range(num_sellers - 1):
            seller = Seller(sell_min_price)
            seller_list.append(seller)
        self.buyers = buyer_list
        self.sellers = seller_list
