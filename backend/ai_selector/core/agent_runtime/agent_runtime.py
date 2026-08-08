from core.agent_runtime.agent_registry import AgentRegistry


class AgentRuntime:

    def __init__(self):
        self.registry = AgentRegistry()


    def register(self, name, agent):
        self.registry.register(
            name,
            agent
        )


    def run(self, context=None):

        if context is None:
            context = {}

        return {
            "agents": list(self.registry.agents.keys()),
            "context": context,
            "status": "completed"
        }