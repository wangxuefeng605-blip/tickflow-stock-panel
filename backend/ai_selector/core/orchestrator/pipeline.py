from .context import AIFlowContext


class AIOrchestrator:


    def __init__(
        self,
        dependencies
    ):

        self.ranking = dependencies.ranking
        self.decision = dependencies.decision
        self.strategy = dependencies.strategy
        self.execution = dependencies.execution



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


        context.strategy = self.strategy.select(
            market
        )


        context.orders = self.execution.execute(
            context.strategy
        )


        return context