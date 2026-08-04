from .runtime_execution_planner import RuntimeExecutionPlanner
from .scanner.runtime_integration import ScannerRuntimeIntegration


class RuntimeExecutionBridge:


    def __init__(self):

        self.planner = RuntimeExecutionPlanner()

        self.runtime = ScannerRuntimeIntegration()



    def execute(self):

        plan = self.planner.plan()


        result = self.runtime.run(
            plan
        )


        return {

            "plan": plan,

            "runtime": result,

            "execution_completed": True

        }