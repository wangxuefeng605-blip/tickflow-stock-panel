class WeightManager:

    def __init__(self):
        self.weights = {
            "momentum": 1.0,
            "trend": 1.0,
            "volume": 1.0,
        }

    def load(self):
        return self.weights

    def save(self, weights):
        self.weights = weights

    def current(self):
        return self.weights