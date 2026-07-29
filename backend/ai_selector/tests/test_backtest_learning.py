from core.backtest.learning import BacktestLearningEngine
from core.backtest.models import BacktestResult
from core.backtest.models import (
    BacktestResult
)


def mock_result():

    return BacktestResult(
        total_return=0.1,
        max_drawdown=0.05,
        trades=[]
    )


def test_learning_engine():

    engine = BacktestLearningEngine()

    signal = engine.analyze(
        mock_result()
    )


    assert signal.return_rate == 0.1

    assert signal.score > 0