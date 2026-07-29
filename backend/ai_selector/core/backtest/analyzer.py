from .models import BacktestResult


class BacktestAnalyzer:


    def analyze(
        self,
        result: BacktestResult
    ):

        return {
            "return": result.total_return,
            "drawdown": result.max_drawdown,
            "trades": len(result.trades)
        }