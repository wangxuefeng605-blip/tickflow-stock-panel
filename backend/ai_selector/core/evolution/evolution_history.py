class EvolutionHistory:

    def __init__(self):
        self.records = []


    def add(
        self,
        generation,
        policy
    ):

        self.records.append(
            {
                "generation": generation,
                "policy": policy.version,
                "score": policy.score
            }
        )


    def latest(self):

        if not self.records:
            return None

        return self.records[-1]