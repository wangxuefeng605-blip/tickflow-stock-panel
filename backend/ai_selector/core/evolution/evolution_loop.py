from core.evolution.evolution_engine import EvolutionEngine
from core.evolution.strategy_mutation import StrategyMutation


class PolicyAdapter:

    def __init__(
        self,
        version,
        score
    ):
        self.version = version
        self.score = score


class EvolutionLoop:


    def __init__(self):

        self.engine = EvolutionEngine()
        self.mutation = StrategyMutation()



    def run(self, result):

        policy = PolicyAdapter(
            version=result.get(
                "strategy",
                "unknown"
            ),
            score=result.get(
                "score",
                0
            )
        )


        evolved = self.engine.evolve(
            policy,
            policy
        )


        return {
            "strategy": policy.version,
            "score": policy.score,
            "mutation": "increase_weight"
        }