from .ai_runtime_governor import AIRuntimeGovernor
from .adaptive_scanner_controller import AdaptiveScannerController


class AutonomousScannerRuntime:


    def __init__(self):

        self.governor = AIRuntimeGovernor()

        self.controller = AdaptiveScannerController()



    def run(self, state):

        decision = self.governor.evaluate(
            state
        )


        config = self.controller.adjust(
            decision
        )


        return {

            "decision": decision,

            "scanner_config": config,

            "autonomous": True

        }