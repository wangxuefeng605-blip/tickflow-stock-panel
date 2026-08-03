class Portfolio:

    def __init__(self):
        self.cash = 100000
        self.positions = {}


    def buy(
        self,
        code,
        qty,
        price
    ):
        self.positions[code]={
            "qty":qty,
            "price":price
        }