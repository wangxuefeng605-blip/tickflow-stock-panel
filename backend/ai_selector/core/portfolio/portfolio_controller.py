"""
Portfolio Controller

Stage32 Portfolio Intelligence Layer
"""


from .portfolio_state import PortfolioState
from .portfolio_risk_engine import PortfolioRiskEngine
from .capital_allocator import CapitalAllocator



class PortfolioController:


    def __init__(self):

        self.risk_engine = PortfolioRiskEngine()

        self.allocator = CapitalAllocator()



    def build(
        self,
        context
    ):

        portfolio = PortfolioState(
            cash=context["capital"]
        )


        risk = self.risk_engine.evaluate(
            portfolio
        )


        allocation = self.allocator.allocate(
            context["signals"],
            context["capital"]
        )


        return {

            "risk": risk["risk"],

            "allocation": allocation

        }