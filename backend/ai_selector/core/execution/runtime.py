from .execution_engine import ExecutionEngine
from .executor import Executor
from .execution_state import ExecutionState



class ExecutionRuntime:


    def __init__(
        self,
        engine=None,
        executor=None,
        state=None
    ):

        self.engine = (
            engine
            or ExecutionEngine()
        )

        self.executor = (
            executor
            or Executor()
        )

        self.state = (
            state
            or ExecutionState()
        )



    def execute(
        self,
        decision
    ):


        plan = (
            self.engine.create_plan(
                decision
            )
        )


        order = (
            self.executor.execute(
                decision
            )
        )


        if order:

            self.state.update(
                plan
            )


        return order