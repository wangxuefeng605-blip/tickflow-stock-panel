from core.runtime.portfolio_runtime_api import PortfolioRuntimeAPI


def test_portfolio_runtime_api():

    api = PortfolioRuntimeAPI()

    result = api.execute(
        {
            "reward": 1,
            "performance": {
                "return": 0.2
            }
        }
    )

    assert result is not None


def test_portfolio_runtime_api_process():

    api = PortfolioRuntimeAPI()

    result = api.process(
        {
            "reward": 0
        }
    )

    assert result is not None