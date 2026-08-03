class PortfolioAllocator:

    def __init__(
        self,
        max_position=0.2
    ):
        self.max_position = max_position


    def allocate(
        self,
        score,
        confidence,
        cash,
        price=10
    ):

        strength = (
            score *
            confidence
        )


        allocation = min(
            strength,
            self.max_position
        )


        amount = (
            cash *
            allocation
        )


        qty = int(
            amount / price
        )


        return {

            "allocation": allocation,

            "amount": amount,

            "qty": qty

        }