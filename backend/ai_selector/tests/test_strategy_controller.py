from core.strategy.strategy_controller import StrategyController


def test_strategy_controller():

    controller = StrategyController()


    result = controller.process(
        "momentum",
        {
            "return":0.15,
            "risk":0.2,
            "win_rate":0.65
        }
    )


    assert result["action"] == "KEEP"