from core.backtest.engine import BacktestEngine


class BacktestAdapter:


    def __init__(
        self,
        engine=None
    ):

        self.engine = engine or BacktestEngine()



    def run(
        self,
        execution
    ):

        if isinstance(execution, dict):

            execution = [
                execution
            ]


        return self.engine.run(
            execution
        )