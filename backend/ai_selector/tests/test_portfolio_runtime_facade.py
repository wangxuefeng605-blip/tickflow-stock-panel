from core.runtime.portfolio_runtime_facade import (
    PortfolioRuntimeFacade
)



def test_portfolio_runtime_facade():


    facade = PortfolioRuntimeFacade()


    result = facade.execute(
        {
            "reward": 1,
            "performance": {
                "return": 0.2
            }
        }
    )


    assert result["adjustment"] == "increase"