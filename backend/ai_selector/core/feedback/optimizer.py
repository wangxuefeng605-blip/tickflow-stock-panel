class WeightOptimizer:

    def optimize(self, learning_result):

        score = learning_result["score"]

        if score >= 0.8:
            weight = 1.10
        elif score >= 0.6:
            weight = 1.00
        else:
            weight = 0.90

        return {
            "weight": weight,
            "samples": learning_result["samples"],
            "status": "UPDATED",
        }