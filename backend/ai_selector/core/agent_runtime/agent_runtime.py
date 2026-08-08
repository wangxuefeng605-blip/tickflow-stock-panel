from core.agent_runtime.agent_registry import AgentRegistry


class AgentRuntime:

    def __init__(self):
        self.registry = AgentRegistry()


    def register(self, name, agent):
        self.registry.register(
            name,
            agent
        )


    def run(self):

        return {
            "agents": self.registry.list_agents()
        }