from core.backtest.engine import BacktestEngine


class BacktestAdapter:


    def __init__(self):

        self.engine = BacktestEngine()


    def run(self, execution):

        return self.engine.run(
            execution
        )