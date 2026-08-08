class AgentCoordinator:

    def __init__(self):
        self.agents = {}


    def register(self, name, agent):
        self.agents[name] = agent


    def coordinate(self, context):

        results = {}

        for name, agent in self.agents.items():

            if hasattr(agent, "run"):
                results[name] = agent.run(context)

        return {
            "context": context,
            "results": results
        }