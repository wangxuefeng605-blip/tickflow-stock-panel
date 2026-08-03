def build_default_dependencies():

    from core.ranking.pipeline import RankingPipeline
    from core.learning.weight_provider import LearningWeightProvider

    from core.intelligence.decision_engine import AIDecisionEngine
    from core.intelligence.portfolio_engine import PortfolioEngine
    from core.strategy.selector import StrategySelector
    from .adapters.backtest_adapter import BacktestAdapter
   
    from core.learning.weight_provider import LearningWeightProvider


    weight_provider = LearningWeightProvider()


    return {

        "ranking": RankingPipeline(
            weight_provider
        ),

    }
    