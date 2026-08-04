class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveKnowledgeTransferEngine:
    """
    Transfers successful evolution knowledge between generations.
    """

    def __init__(self):

        self.knowledge = []

        self.history = []


    def store_knowledge(self, strategy):

        self.knowledge.append(
            strategy
        )


        self.history.append(
            {
                "action": "store",
                "strategy": strategy
            }
        )


        return strategy



    def transfer(self, target_strategy):

        if not self.knowledge:

            return None


        source = self.knowledge[-1]


        result = {

            "target": target_strategy,

            "inherited_from": source,

            "status": "transferred"

        }


        self.history.append(
            {
                "action": "transfer",
                "result": result
            }
        )


        return result



    def get_knowledge(self):

        return self.knowledge



    def get_history(self):

        return self.history