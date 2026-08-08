from .agent_reasoner import AgentReasoner


class AgentController:

    def __init__(self):

        self.reasoner = AgentReasoner()

        self.history = []


    def run(self, context):

        decision = self.reasoner.reason(
            context
        )

        self.history.append(
            decision
        )

        return decision