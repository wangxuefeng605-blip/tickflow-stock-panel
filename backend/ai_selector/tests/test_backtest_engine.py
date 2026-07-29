from core.backtest.engine import BacktestEngine


def test_backtest_engine():

    engine=BacktestEngine()


    result=engine.run(
        [
            {
                "code":"000001",
                "return":0.1
            },
            {
                "code":"000002",
                "return":-0.05
            }
        ]
    )


    assert result["trades"]==2

    assert result["total_return"]==0.05