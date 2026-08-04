from .runtime_adaptive_governor import RuntimeAdaptiveGovernor


class RuntimeExecutionPlanner:


    def __init__(self):

        self.governor = RuntimeAdaptiveGovernor()



    def plan(self):

        config = self.governor.decide()


        tasks = [
            "scan_pool",
            "calculate_factor",
            "rank_stock"
        ]


        if config["runtime_mode"] == "SAFE":

            tasks = [
                "scan_pool"
            ]


        return {

            "mode": config["runtime_mode"],

            "workers": config["workers"],

            "retry_enabled": config["retry_enabled"],

            "tasks": tasks

        }