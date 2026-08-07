"""
Runtime State

Stage34 Autonomous Runtime
"""


class RuntimeState:


    def __init__(self):

        self.state = {

            "decision": {},

            "execution": {},

            "portfolio": {},

            "strategy": {},

            "learning": {}

        }


    def update(
        self,
        key,
        value
    ):

        self.state[key] = value


    def get(
        self,
        key
    ):

        return self.state.get(
            key,
            {}
        )


    def snapshot(self):

        return self.state.copy()