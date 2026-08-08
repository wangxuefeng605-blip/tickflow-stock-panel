"""
Runtime Controller

Stage34 Autonomous Runtime
"""


from .autonomous_runtime import AutonomousRuntime


class RuntimeController:


    def __init__(self):

        self.runtime = AutonomousRuntime()



    def execute(
        self,
        context
    ):

        return self.runtime.run(
            context
        )