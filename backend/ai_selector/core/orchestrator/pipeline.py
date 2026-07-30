from .context import AIFlowContext


class Dependencies:

    pass


class AIOrchestrator:


    def __init__(
        self,
        dependencies=None
    ):

        if dependencies is None or dependencies == {}:
            dependencies = self.default_dependencies()


        def resolve(name):

            if isinstance(dependencies, dict):
                return dependencies.get(name)

            return getattr(
                dependencies,
                name,
                None
            )


        self.ranking = resolve("ranking")
        self.decision = resolve("decision")
        self.portfolio = resolve("portfolio")
        self.strategy = resolve("strategy")
        self.execution = resolve("execution")


        self.backtest = resolve("backtest")
        self.learning = resolve("learning")
        

    def default_dependencies(self):

        from core.ranking.pipeline import RankingPipeline
        from core.orchestrator.adapters.ranking_adapter import RankingAdapter
        from core.orchestrator.adapters.decision_adapter import DecisionAdapter

        from core.intelligence.decision_engine import AIDecisionEngine
        from core.strategy.selector import StrategySelector

        from core.orchestrator.adapters.execution_adapter import ExecutionAdapter
        from core.execution.engine import ExecutionEngine

        from core.intelligence.portfolio_engine import PortfolioEngine

        from core.orchestrator.adapters.backtest_adapter import BacktestAdapter
        from core.backtest.engine import BacktestEngine

        from core.learning.orchestrator_hook import LearningOrchestratorHook


        deps = Dependencies()
    


        deps.ranking = RankingAdapter(
            RankingPipeline()
        )

        deps.decision = DecisionAdapter(
            AIDecisionEngine()
        )

        deps.portfolio = PortfolioEngine()

        deps.strategy = StrategySelector()

        deps.execution = ExecutionAdapter(
            ExecutionEngine()
        )
        deps.backtest = BacktestAdapter(
            BacktestEngine()
        )

        deps.learning = LearningOrchestratorHook()

        return deps



    def run(
        self,
        market
    ):

        context = AIFlowContext()


        context.ranking = self.ranking.run(
            market
        )


        context.decision = self.decision.run(
            context.ranking
        )


        if self.portfolio:

            context.portfolio = self.portfolio.evaluate(
                {
                    "code": context.decision[0].code,
                    "score": context.decision[0].score,
                    "confidence": context.decision[0].confidence
                }
            )

        else:

            context.portfolio = None


        context.strategy = self.strategy.select(
            market
        )


        context.orders = self.execution.execute(
            context.decision
        )


        if self.backtest:

           context.backtest = self.backtest.run(
                context.orders
            )

        else:

            context.backtest = None

        if self.learning:

            context.learning = self.learning.after_backtest(
                {
                    "backtest": context.backtest
                }
            )

            context.learning_updated = True

        else:

            context.learning_updated = False
   
        return context

        