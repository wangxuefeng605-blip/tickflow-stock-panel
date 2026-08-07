from core.execution.execution_controller import ExecutionController


def test_stage31_full_execution_loop():

    controller = ExecutionController()


    result = controller.run(
        {
            "action": "BUY",
            "symbol": "000001",
            "price": 10,
            "exit_price": 13,
            "confidence": 0.95,
            "risk": 0.1
        }
    )


    assert result["status"] == "SUCCESS"

    assert result["reward"] > 0