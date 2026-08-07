from core.execution.execution_feedback import ExecutionFeedback


def test_execution_feedback():

    feedback = ExecutionFeedback()


    result = feedback.collect(
        {
            "symbol": "000001",
            "action": "BUY",
            "status": "EXECUTED",
            "price": 10,
            "exit_price": 12
        }
    )


    assert result["symbol"] == "000001"

    assert result["reward"] > 0

    assert result["status"] == "SUCCESS"