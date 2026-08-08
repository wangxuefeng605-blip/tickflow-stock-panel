from core.evolution.policy_mutation import PolicyMutation
from core.evolution.policy_crossover import PolicyCrossover
from core.evolution.evolution_history import EvolutionHistory


class EvolutionEngine:

    def __init__(self):

        self.mutation = PolicyMutation()
        self.crossover = PolicyCrossover()
        self.history = EvolutionHistory()


    def evolve(self, policy_a, policy_b):

        mutated = self.mutation.mutate(
            policy_a
        )

        child = self.crossover.crossover(
            mutated,
            policy_b
        )

        self.history.add(
            1,
            child
        )

        return child