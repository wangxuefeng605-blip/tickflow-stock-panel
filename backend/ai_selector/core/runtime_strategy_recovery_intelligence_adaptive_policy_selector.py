class RuntimeStrategyRecoveryIntelligenceAdaptivePolicySelector:
    """
    Selects the best recovery policy dynamically.
    """

    def __init__(self):

        self.policies = []
        self.history = []


    def register_policy(self, policy):

        self.policies.append(policy)


    def select(self, context=None):

        if not self.policies:

            result = {
                "policy": None,
                "score": 0
            }

        else:

            selected = max(
                self.policies,
                key=lambda x: x.get(
                    "policy_score",
                    0
                )
            )

            result = {
                "policy": selected.get(
                    "policy_version"
                ),
                "score": selected.get(
                    "policy_score"
                )
            }


        self.history.append(result)

        return result


    def get_history(self):

        return self.history