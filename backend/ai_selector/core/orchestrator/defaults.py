def build_default_dependencies():

    from core.ranking.pipeline import RankingPipeline
    from core.intelligence.decision_engine import AIDecisionEngine
    from core.intelligence.portfolio_engine import PortfolioEngine
    from core.strategy.selector import StrategySelector
    from .adapters.backtest_adapter import BacktestAdapter


    return {

        "ranking": RankingPipeline(),

        "decision": AIDecisionEngine(),

        "portfolio": PortfolioEngine(),

        "strategy": StrategySelector(),

        "execution": None

    }