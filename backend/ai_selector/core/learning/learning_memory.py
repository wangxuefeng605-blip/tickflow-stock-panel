class LearningMemory:

    def __init__(self):
        self.storage = []


    def save(self, data):

        self.storage.append(data)

        return data


    def get_all(self):

        return self.storage