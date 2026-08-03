from .position import Position


class Portfolio:

    def __init__(self):
        self.cash = 100000
        self.positions = {}


    def buy(
        self,
        code,
        price,
        qty
    ):

        cost = price * qty

        self.cash -= cost

        self.positions[code] = {
            "qty": qty,
            "price": price
        }

        return True


    def apply(self, order):

        if order["action"] == "BUY":

            return self.buy(
                order["code"],
                order["price"],
                order["qty"]
            )

        return False


    def state(self):

        return {
            "cash": self.cash,
            "positions": self.positions
        }