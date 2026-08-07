"""
Capital Allocator

Stage32 Portfolio Intelligence Layer
"""


class CapitalAllocator:


    def allocate(
        self,
        scores,
        capital
    ):

        total = sum(
            scores.values()
        )


        allocation = {}


        for symbol, score in scores.items():

            allocation[symbol] = round(
                capital *
                score /
                total,
                2
            )


        return allocation