from .simulator import Simulator
from .metrics import calculate_metrics


class BacktestEngine:


    def __init__(self):

        self.simulator=Simulator()


    def run(
        self,
        signals
    ):

        trades=self.simulator.simulate(
            signals
        )


        metrics=calculate_metrics(
            trades
        )


        return metrics