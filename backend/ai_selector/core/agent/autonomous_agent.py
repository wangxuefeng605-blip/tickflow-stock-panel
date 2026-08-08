from .agent_state import AgentState
from .agent_memory import AgentMemory
from .agent_controller import AgentController


class AutonomousAgent:

    def __init__(self):

        self.state = AgentState()

        self.memory = AgentMemory()

        self.controller = AgentController()


    def act(self, context):

        result = self.controller.run(
            context
        )

        self.memory.remember(
            result
        )

        return result