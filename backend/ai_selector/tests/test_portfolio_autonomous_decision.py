from core.portfolio.autonomous_engine import (
    AutonomousPortfolioEngine
)


class MockStrategy:

    def evolve(
        self,
        market,
        signal
    ):

        return {
            "confidence":0.8
        }



class MockAllocator:

    def allocate(
        self,
        strategy
    ):

        return 0.5



class MockRisk:

    def check(
        self,
        allocation
    ):

        return True



engine = AutonomousPortfolioEngine(
    MockStrategy(),
    MockAllocator(),
    MockRisk()
)



def test_autonomous_portfolio_decision():

    result = engine.decide(
        market="BULL",
        signal={
            "reward":0.8,
            "risk":0.1
        }
    )


    assert result["action"] == "BUY"

    assert result["allocation"] > 0