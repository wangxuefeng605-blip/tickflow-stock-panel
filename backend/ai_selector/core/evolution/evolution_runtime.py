from core.evolution.evolution_controller import EvolutionController


class EvolutionRuntime:

    def __init__(self):
        self.controller = EvolutionController()


    def run(self, strategy):

        result = self.controller.evolve(strategy)

        return {
            **result,
            "status": "EVOLVED"
        }