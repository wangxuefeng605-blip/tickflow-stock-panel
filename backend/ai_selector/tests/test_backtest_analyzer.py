from core.backtest.analyzer import BacktestAnalyzer
from core.backtest.models import BacktestResult


def test_backtest_analyzer():

    result = BacktestResult(
        total_return=0.1,
        max_drawdown=0.05,
        trades=[]
    )

    analysis = BacktestAnalyzer().analyze(
        result
    )

    assert analysis is not None