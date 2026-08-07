from core.execution.execution_simulator import ExecutionSimulator


def test_execution_simulator():

    simulator = ExecutionSimulator()


    result = simulator.execute(
        {
            "action": "BUY",
            "symbol": "000001",
            "price": 10
        }
    )


    assert result["status"] == "EXECUTED"

    assert result["symbol"] == "000001"