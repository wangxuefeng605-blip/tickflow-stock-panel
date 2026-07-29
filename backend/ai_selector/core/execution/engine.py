class ExecutionEngine:


    def execute(
        self,
        decisions
    ):

        orders = []


        for decision in decisions:

            orders.append(
                {
                    "code": decision.code,
                    "action": decision.action,
                    "status": "READY"
                }
            )


        return {

            "status": "CREATED",

            "orders": orders

        }