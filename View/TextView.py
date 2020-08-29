"""
The simplest view possible only built out to display data from a market in printed form.
"""


class TextView:

    def __init__(self):
        pass

    @staticmethod
    def show_stats(successful_sellers, successful_buyers, average_seller_profit, average_buyer_surplus):
        print('successful sellers: {}'.format(successful_sellers))
        print('successful buyers: {}'.format(successful_buyers))
        print('average seller profit: {}'.format(average_seller_profit))
        print('average_buyer_surplus: {}'.format(average_buyer_surplus))