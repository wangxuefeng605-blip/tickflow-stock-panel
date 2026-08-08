class AgentMemory:

    def __init__(self):
        self.records = []


    def remember(self, item):

        self.records.append(item)


    def recent(self, limit=5):

        return self.records[-limit:]


    def size(self):

        return len(self.records)