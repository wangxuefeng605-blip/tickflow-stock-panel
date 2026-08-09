"""
Realtime Score Engine
"""

class RealtimeScoreEngine:

    def calculate(self, factors):

        score = (
            factors.get("momentum",0)
            +
            factors.get("trend",0)
        ) / 2


        return {
            "score": score
        }