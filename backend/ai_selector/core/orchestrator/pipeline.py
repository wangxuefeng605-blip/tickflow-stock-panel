class AIPipeline:

    def run(self):

        stocks = scanner.scan()

        ranking = ranking_engine.rank(
            stocks
        )

        decision = decision_engine.decide(
            ranking
        )

        strategy = strategy_engine.generate(
            decision
        )

        execution = executor.execute(
            strategy
        )

        return execution