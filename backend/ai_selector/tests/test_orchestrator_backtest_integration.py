result = engine.run(
    market="BULL",
    mode="BACKTEST"
)

assert result.backtest.total_return is not None