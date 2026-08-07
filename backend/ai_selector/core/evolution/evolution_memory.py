"""
Evolution Memory

Stage28 Self Evolution Layer
"""


class EvolutionMemory:


    def __init__(self):

        self.history = []


    def save_strategy(
        self,
        strategy,
        score=None
    ):

        self.history.append(
            strategy
        )

        return True



    def load_history(self):

        return self.history



    def record_result(
        self,
        strategy_id,
        result
    ):

        for item in self.history:

            if item.get("id") == strategy_id:

                item["result"] = result

                return True

        return False



    def best_strategy(self):

        if not self.history:

            return None


        ranked = sorted(
            self.history,
            key=lambda x:
                x.get(
                    "score",
                    0
                ),
            reverse=True
        )


        return ranked[0]