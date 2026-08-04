from copy import deepcopy


class RuntimeStrategyAutoRecoveryManager:
    """
    Runtime strategy recovery controller.

    Responsibilities:
    - keep last valid state
    - recover after failure
    - rollback invalid state
    - fallback strategy
    """

    def __init__(self):

        self.current_state = None
        self.last_valid_state = None

        self.recovery_count = 0


    def save_checkpoint(self, state):

        self.last_valid_state = deepcopy(state)

        self.current_state = deepcopy(state)

        return {
            "saved": True,
            "state": self.last_valid_state
        }


    def update_state(self, state):

        self.current_state = deepcopy(state)

        return self.current_state


    def validate_state(self, state):

        if not isinstance(state, dict):

            return False

        if "strategy" not in state:

            return False

        return True


    def recover(self):

        if self.last_valid_state is None:

            return {
                "recovered": False
            }

        self.current_state = deepcopy(
            self.last_valid_state
        )

        self.recovery_count += 1

        return {
            "recovered": True,
            "state": self.current_state
        }


    def rollback_if_invalid(self):

        if self.validate_state(
            self.current_state
        ):

            return {
                "rollback": False,
                "state": self.current_state
            }


        return {
            "rollback": True,
            **self.recover()
        }


    def fallback_strategy(self):

        self.current_state = {
            "strategy": "default",
            "version": 1
        }

        return {
            "fallback": True,
            "state": self.current_state
        }