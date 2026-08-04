from core.runtime_strategy_state_storage import (
    RuntimeStrategyStateStorage
)

from core.runtime_strategy_state_validator import (
    RuntimeStrategyStateValidator
)


class RuntimeStrategyLifecycleManager:
    """
    Runtime Strategy lifecycle controller.
    """

    def __init__(self, storage=None, validator=None):

        self.storage = (
            storage
            or RuntimeStrategyStateStorage()
        )

        self.validator = (
            validator
            or RuntimeStrategyStateValidator()
        )

        self.state = {}

        self.active = False


    def initialize(self):

        result = self.storage.load()

        if result["loaded"]:

            self.state = result["state"]

        else:

            self.state = {
                "strategy": "default",
                "version": 1
            }

        return self.state


    def validate(self):

        return self.validator.validate(
            self.state
        )


    def activate(self):

        if not self.validate():

            return {
                "activated": False
            }

        self.active = True

        return {
            "activated": True,
            "state": self.state
        }


    def update(self, changes):

        self.state.update(
            changes
        )

        return self.state


    def persist(self):

        return self.storage.save(
            self.state
        )


    def lifecycle(self):

        self.initialize()

        validation = self.validate()

        if not validation:

            return {
                "success": False
            }

        self.activate()

        self.persist()

        return {
            "success": True,
            "state": self.state
        }