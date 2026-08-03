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


        if cost > self.cash:
            return False


        self.cash -= cost


        self.positions[code] = Position(
            code,
            qty,
            price
        )


        return True



    def sell(
        self,
        code
    ):

        if code not in self.positions:
            return False


        position = self.positions.pop(code)


        self.cash += position.value()


        return True



    def apply(
        self,
        order
    ):


        action = order.get(
            "action"
        )


        if action == "BUY":

            return self.buy(
                order["code"],
                order["price"],
                order["qty"]
            )


        if action == "SELL":

            return self.sell(
                order["code"]
            )


        return False