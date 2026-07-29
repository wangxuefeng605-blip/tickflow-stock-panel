from core.backtest.engine import BacktestEngine
from core.backtest.models import BacktestRequest


def test_backtest_engine_flow():

    engine = BacktestEngine()


    result = engine.run(
        BacktestRequest()
    )


    assert result is not None