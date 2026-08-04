class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionExperienceRetriever:
    """
    Retrieves useful evolution experiences.
    """

    def __init__(self):

        self.experiences = []


    def add_experience(self, experience):

        self.experiences.append(
            experience
        )

        return experience



    def retrieve_best(self):

        if not self.experiences:

            return None


        return max(
            self.experiences,
            key=lambda x: x.get(
                "fitness",
                0
            )
        )



    def retrieve_success(self):

        return [

            e for e in self.experiences

            if e.get(
                "fitness",
                0
            ) >= 0.5

        ]



    def retrieve_failure(self):

        return [

            e for e in self.experiences

            if e.get(
                "fitness",
                0
            ) < 0.5

        ]



    def get_history(self):

        return self.experiences