"""
Meta Learning State

Stage37 Meta Learning
"""


class MetaState:


    def __init__(self):

        self.cycles = 0

        self.best_strategy = None

        self.optimizations = 0

        self.success_rate = 0.0



    def record_cycle(
        self,
        success
    ):

        self.cycles += 1


        if success:
            self.optimizations += 1


        self.success_rate = (
            self.optimizations /
            self.cycles
        )


    def update_best_strategy(
        self,
        strategy
    ):

        self.best_strategy = strategy



    def snapshot(self):

        return {

            "cycles":
                self.cycles,

            "best_strategy":
                self.best_strategy,

            "optimizations":
                self.optimizations,

            "success_rate":
                self.success_rate
        }