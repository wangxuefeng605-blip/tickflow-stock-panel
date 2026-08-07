"""
Portfolio State

Stage32 Portfolio Intelligence Layer
"""


class PortfolioState:


    def __init__(
        self,
        cash=0
    ):

        self.cash = cash

        self.positions = {}



    def add_position(
        self,
        symbol,
        shares,
        cost
    ):

        self.positions[symbol] = {

            "shares": shares,

            "cost": cost
        }



    def total_cost(self):

        total = 0


        for position in self.positions.values():

            total += (
                position["shares"]
                *
                position["cost"]
            )


        return total



    def exposure(self):

        if self.cash == 0:

            return 0


        return (
            self.total_cost()
            /
            self.cash
        )