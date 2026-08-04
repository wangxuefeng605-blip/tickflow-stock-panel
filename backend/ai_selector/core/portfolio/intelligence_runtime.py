from .autonomous_engine import AutonomousPortfolioEngine
from .strategy_evolver import StrategyEvolver
from .portfolio_feedback import PortfolioFeedback
from .runtime_state import PortfolioRuntimeState
from .allocation_optimizer import AllocationOptimizer
from .risk_engine import PortfolioRiskEngine
from core.portfolio.intelligence import PortfolioIntelligence
from core.learning.portfolio_adapter import PortfolioLearningAdapter


class PortfolioIntelligenceRuntime:


    def __init__(self):

        self.evolver = StrategyEvolver()

        self.feedback = PortfolioFeedback()

        self.state = PortfolioRuntimeState()


        self.engine = AutonomousPortfolioEngine(
            strategy=self.evolver,
            allocator=AllocationOptimizer(),
            risk=PortfolioRiskEngine()
        )

        self.learning = PortfolioLearningAdapter()



    def run(
        self,
        feedback
    ):

        result = self.feedback.process(
            feedback
        )


        learning_result = self.learning.update(
            feedback
        )


        reward = feedback.get(
            "reward",
            0
        )


        if reward > 0:
            adjustment = "increase"
        elif reward < 0:
            adjustment = "decrease"
        else:
            adjustment = "hold"



        return {

            "feedback": result,

            "learning": learning_result,

            "adjustment": adjustment

        }


    def execute(
        self,
        market,
        signals
    ):


        strategy = self.evolver.evolve(
            market,
            signals
        )


        decision = self.engine.decide(
            market=market,
            signal=signals
        )


        result = {

            "strategy": strategy,

            "decision": decision,

            "learning": True

        }


        self.state.update({

            "last_strategy": strategy,

            "last_decision": decision,

            "learning_updated": True

        })


        return result