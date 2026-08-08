"""
Evolution Decision Engine

Stage54
"""


class EvolutionDecision:


    def decide(
        self,
        current,
        candidates
    ):

        best = max(
            candidates,
            key=lambda x:x["reward"]
        )


        if best["reward"] > current["reward"]:

            return {
                "decision":"REPLACE",
                "strategy":best
            }


        return {
            "decision":"KEEP",
            "strategy":current
        }