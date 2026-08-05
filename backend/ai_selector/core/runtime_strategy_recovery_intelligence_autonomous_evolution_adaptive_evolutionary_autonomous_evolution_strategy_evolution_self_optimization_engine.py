class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelfOptimizationEngine:
    """
    Optimizes strategy parameters automatically.
    """

    def __init__(self):

        self.parameters = {}

        self.optimization_history = []

        self.history = []



    def register_strategy(
        self,
        name,
        parameters=None
    ):

        self.parameters[name] = parameters or {}


        result = {

            "strategy": name,

            "registered": True

        }


        self.history.append(
            {
                "action": "register",
                "result": result
            }
        )


        return result



    def update_parameter(
        self,
        name,
        key,
        value
    ):

        if name not in self.parameters:

            return None


        self.parameters[name][key] = value


        result = {

            "strategy": name,

            "parameter": key,

            "value": value

        }


        self.history.append(
            {
                "action": "update",
                "result": result
            }
        )


        return result



    def optimize(
        self,
        name,
        feedback_score
    ):

        if name not in self.parameters:

            return None


        factor = 1


        if feedback_score < 0:

            factor = 0.9

        else:

            factor = 1.1



        optimized = {}


        for key, value in self.parameters[name].items():

            if isinstance(value, (int, float)):

                optimized[key] = round(
                    value * factor,
                    3
                )

            else:

                optimized[key] = value



        self.parameters[name] = optimized


        result = {

            "strategy": name,

            "factor": factor,

            "parameters": optimized

        }


        self.optimization_history.append(
            result
        )


        self.history.append(
            {
                "action": "optimize",
                "result": result
            }
        )


        return result



    def compare(
        self,
        name
    ):

        return self.parameters.get(
            name
        )



    def get_history(self):

        return self.history