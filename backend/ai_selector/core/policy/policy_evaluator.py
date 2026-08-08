class PolicyEvaluator:

    def evaluate(
        self,
        policy,
        performance
    ):

        score = performance.get(
            "score",
            0.0
        )

        policy.update_score(score)

        return {
            "version": policy.version,
            "score": score,
            "active": policy.active
        }