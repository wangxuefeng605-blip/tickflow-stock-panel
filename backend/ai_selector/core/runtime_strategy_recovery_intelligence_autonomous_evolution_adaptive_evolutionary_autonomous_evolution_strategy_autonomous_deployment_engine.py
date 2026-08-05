class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyAutonomousDeploymentEngine:
    """
    Deploys validated strategies automatically.
    """

    def __init__(self):

        self.candidates = {}

        self.deployed = {}

        self.history = []



    def register_candidate(
        self,
        name,
        score
    ):

        self.candidates[name] = {

            "score": score,

            "status": "candidate"

        }


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



    def validate(
        self,
        name,
        threshold=0.7
    ):

        candidate = self.candidates.get(
            name
        )


        if not candidate:

            return None


        result = {

            "strategy": name,

            "approved":
                candidate["score"] >= threshold

        }


        self.history.append(
            {
                "action": "validate",
                "result": result
            }
        )


        return result



    def deploy(
        self,
        name
    ):

        validation = self.validate(
            name
        )


        if not validation or not validation["approved"]:

            return {

                "deployed": False

            }


        self.deployed[name] = {

            "status": "running",

            "score":
                self.candidates[name]["score"]

        }


        result = {

            "strategy": name,

            "deployed": True

        }


        self.history.append(
            {
                "action": "deploy",
                "result": result
            }
        )


        return result



    def rollback(
        self,
        name
    ):

        if name in self.deployed:

            self.deployed[name]["status"] = "rollback"


        result = {

            "strategy": name,

            "rolled_back": True

        }


        self.history.append(
            {
                "action": "rollback",
                "result": result
            }
        )


        return result



    def get_deployed(self):

        return self.deployed



    def get_history(self):

        return self.history