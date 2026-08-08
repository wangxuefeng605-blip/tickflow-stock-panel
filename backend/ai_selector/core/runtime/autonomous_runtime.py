"""
Autonomous Runtime

Stage34 Autonomous Runtime Integration
"""


from .runtime_state import RuntimeState



class AutonomousRuntime:


    def __init__(self):

        self.state = RuntimeState()



    def run(
        self,
        context
    ):

        for key in [
            "decision",
            "execution",
            "portfolio",
            "strategy",
            "learning"
        ]:

            self.state.update(
                key,
                context.get(
                    key,
                    {}
                )
            )


        return self.state.snapshot()