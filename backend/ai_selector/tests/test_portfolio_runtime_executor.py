from core.runtime.portfolio_runtime_executor import (
    PortfolioRuntimeExecutor
)


def test_portfolio_runtime_executor():

    executor = PortfolioRuntimeExecutor()


    result = executor.execute(
        {
            "reward":1,
            "performance":{
                "return":0.2
            }
        }
    )


    assert result is not None