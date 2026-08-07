class StrategyMutationEngine:

    def mutate(self, strategy):

        return [
            strategy + "_fast",
            strategy + "_safe"
        ]