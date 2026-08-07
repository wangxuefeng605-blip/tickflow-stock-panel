from core.execution.execution_controller import ExecutionController


def test_execution_controller():

    controller = ExecutionController()


    result = controller.run(
        {
            "action": "BUY",
            "symbol": "000001",
            "price": 10,
            "exit_price": 12,
            "confidence": 0.9,
            "risk": 0.1
        }
    )


    assert result["status"] == "SUCCESS"

    assert result["reward"] > 0

    assert result["symbol"] == "000001"