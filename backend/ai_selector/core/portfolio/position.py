class Position:


    def __init__(
        self,
        code,
        qty,
        price
    ):

        self.code = code
        self.qty = qty
        self.price = price


    @property
    def market_value(self):

        return self.qty * self.price