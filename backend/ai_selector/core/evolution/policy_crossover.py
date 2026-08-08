class PolicyCrossover:

    def crossover(
        self,
        policy_a,
        policy_b
    ):

        child = type(policy_a)(
            version=f"{policy_a.version}-{policy_b.version}-child",
            score=max(
                policy_a.score,
                policy_b.score
            )
        )

        return child