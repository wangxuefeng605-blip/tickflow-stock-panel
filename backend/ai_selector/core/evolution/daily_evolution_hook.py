from core.evolution.evolution_runtime import EvolutionRuntime


class DailyEvolutionHook:

    def __init__(self):
        self.runtime = EvolutionRuntime()


    def evolve(self, result):

        return self.runtime.run(
            result
        )