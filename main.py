from Model.Market.BaseMarket import BaseMarket
from View.TextView import TextView
from Controller.SimpleController import SimpleController


def main():
    simple_market = BaseMarket(5000, 5700, 14, 13)
    text_view = TextView()
    controller = SimpleController(text_view, simple_market)
    controller.start()


if __name__ == "__main__":
    main()
