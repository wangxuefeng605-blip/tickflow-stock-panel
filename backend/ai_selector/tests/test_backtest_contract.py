from core.backtest.models import (
    BacktestRequest,
    TradeRecord,
    BacktestResult
)


def test_backtest_models():

    req = BacktestRequest(
        strategy="AI",
        start_date="2025-01-01",
        end_date="2025-12-31",
        capital=100000
    )

    trade = TradeRecord(
        code="000001",
        action="BUY",
        price=10,
        quantity=100
    )

    result = BacktestResult(
        total_return=0.1,
        max_drawdown=0.05,
        trades=[trade]
    )


    assert req.strategy == "AI"
    assert result.total_return == 0.1