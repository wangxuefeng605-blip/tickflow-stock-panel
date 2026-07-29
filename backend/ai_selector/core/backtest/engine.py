from .models import (
    BacktestRequest,
    BacktestResult
)


class BacktestEngine:


    def run(
        self,
        request
    ):

        return BacktestResult(
            trades=[],
            equity_curve=[],
            return_rate=0
        )