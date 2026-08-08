class AgentState:

    def __init__(self):

        self.status = "IDLE"

        self.goal = None

        self.memory = []

        self.last_action = None


    def activate(self):

        self.status = "ACTIVE"


    def record(self, event):

        self.memory.append(event)


    def snapshot(self):

        return {
            "status": self.status,
            "goal": self.goal,
            "memory_size": len(self.memory),
            "last_action": self.last_action
        }