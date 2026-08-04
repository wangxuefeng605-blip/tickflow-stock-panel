class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryPolicyOptimizationEngine:
    """
    Optimizes evolution policies using feedback rewards.
    """

    def __init__(self):

        self.policies = {}

        self.history = []



    def register_policy(
        self,
        name,
        value
    ):

        self.policies[name] = value


        self.history.append(
            {
                "action": "register",
                "policy": name
            }
        )


        return value



    def optimize(
        self,
        name,
        reward
    ):

        if name not in self.policies:

            return None


        old_value = self.policies[name]


        new_value = round(
            old_value + reward * 0.1,
            3
        )


        self.policies[name] = new_value


        result = {

            "policy": name,

            "old_value": old_value,

            "new_value": new_value

        }


        self.history.append(
            {
                "action": "optimize",
                "result": result
            }
        )


        return result



    def get_policy(
        self,
        name
    ):

        return self.policies.get(
            name
        )



    def get_history(self):

        return self.history