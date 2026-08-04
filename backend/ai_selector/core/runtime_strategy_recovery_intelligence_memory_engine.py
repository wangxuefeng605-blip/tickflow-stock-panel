class RuntimeStrategyRecoveryIntelligenceMemoryEngine:
    """
    Long-term memory engine for recovery intelligence.
    """

    def __init__(self):

        self.memory = []


    def remember(self, experience):

        self.memory.append(
            experience
        )

        return {
            "stored": True,
            "size": len(self.memory)
        }


    def recall(self, policy=None):

        if policy is None:
            return self.memory


        return [
            item
            for item in self.memory
            if item.get("policy") == policy
        ]


    def latest(self):

        if not self.memory:
            return None

        return self.memory[-1]


    def history(self):

        return self.memory