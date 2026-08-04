class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceReplayEngine:
    """
    Replays successful evolution experiences.
    """

    def __init__(self):

        self.memory = []
        self.history = []


    def store(self, experience):

        self.memory.append(
            experience
        )


        self.history.append(
            {
                "action": "store",
                "experience": experience
            }
        )


        return experience



    def replay(self):

        if not self.memory:

            return None


        best = max(
            self.memory,
            key=lambda x: x.get(
                "fitness",
                0
            )
        )


        result = {

            "replayed_strategy": best.get(
                "strategy"
            ),

            "fitness": best.get(
                "fitness"
            ),

            "source": "experience_memory"

        }


        self.history.append(
            {
                "action": "replay",
                "result": result
            }
        )


        return result



    def get_memory(self):

        return self.memory



    def get_history(self):

        return self.history