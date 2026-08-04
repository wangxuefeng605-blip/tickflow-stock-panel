class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMemoryEngine:
    """
    Stores autonomous evolution experience memory.
    """

    def __init__(self):

        self.memory = []
        self.success_memory = []
        self.failure_memory = []


    def record(self, evolution):

        self.memory.append(
            evolution
        )


        if evolution.get(
            "fitness",
            0
        ) >= 0.5:

            self.success_memory.append(
                evolution
            )

        else:

            self.failure_memory.append(
                evolution
            )


        return evolution



    def get_best_memory(self):

        if not self.success_memory:

            return None


        return max(
            self.success_memory,
            key=lambda x: x.get(
                "fitness",
                0
            )
        )



    def get_history(self):

        return self.memory



    def get_success_history(self):

        return self.success_memory



    def get_failure_history(self):

        return self.failure_memory