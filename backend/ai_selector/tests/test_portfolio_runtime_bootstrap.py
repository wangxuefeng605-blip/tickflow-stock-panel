from core.runtime.portfolio_runtime_bootstrap import (
    PortfolioRuntimeBootstrap
)


def test_portfolio_runtime_bootstrap():

    runtime = PortfolioRuntimeBootstrap()


    result = runtime.start(
        {
            "reward":1,
            "performance":{
                "return":0.2
            }
        }
    )


    assert result is not None