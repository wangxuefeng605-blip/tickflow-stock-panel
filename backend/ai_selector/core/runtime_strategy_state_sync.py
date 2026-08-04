class RuntimeStrategyStateSynchronizer:
    """
    Runtime strategy state synchronizer.

    Applies updated strategy parameters
    into active runtime state.
    """

    def __init__(self):
        self.state = {}

    def sync(self, parameters):
        self.state.update(parameters)

        return {
            "synced": True,
            "state": self.state
        }

    def get_state(self):
        return self.state