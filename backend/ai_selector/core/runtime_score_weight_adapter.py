class RuntimeScoreWeightAdapter:


    def __init__(self):

        self.weights = {}


    def apply(self, context):

        weight = context.get(
            "weight",
            1.0
        )

        self.weights = {

            "momentum": weight,

            "trend": weight,

            "quality": 1.0

        }

        return self.weights


    def current(self):

        return self.weights