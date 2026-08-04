class RuntimeStrategyRecoveryIntelligenceExperienceReplayEngine:
    """
    Experience replay engine for recovery intelligence.
    """

    def __init__(self):

        self.experiences = []


    def store(self, experience):

        self.experiences.append(
            experience
        )

        return {
            "stored": True,
            "count": len(self.experiences)
        }


    def replay(self, policy):

        matches = [
            item
            for item in self.experiences
            if item.get("policy") == policy
        ]

        if not matches:
            return None

        return matches[-1]


    def replay_all(self):

        return self.experiences


    def get_history(self):

        return self.experiences