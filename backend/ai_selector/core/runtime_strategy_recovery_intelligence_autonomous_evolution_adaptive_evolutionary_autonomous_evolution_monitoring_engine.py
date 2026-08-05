class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMonitoringEngine:
    """
    Monitors autonomous evolution performance.
    """

    def __init__(self):

        self.metrics = {}

        self.history = []



    def record_metric(
        self,
        strategy,
        performance
    ):

        self.metrics[strategy] = performance


        result = {

            "strategy": strategy,

            "performance": performance

        }


        self.history.append(
            {
                "action": "record",
                "result": result
            }
        )


        return result



    def detect_degradation(
        self,
        strategy,
        threshold=0.5
    ):

        performance = self.metrics.get(
            strategy
        )


        if performance is None:

            return None


        degraded = performance < threshold


        result = {

            "strategy": strategy,

            "degraded": degraded,

            "performance": performance

        }


        self.history.append(
            {
                "action": "detect",
                "result": result
            }
        )


        return result



    def evolution_score(self):

        if not self.metrics:

            return 0


        return round(
            sum(self.metrics.values())
            /
            len(self.metrics),
            3
        )



    def get_history(self):

        return self.history