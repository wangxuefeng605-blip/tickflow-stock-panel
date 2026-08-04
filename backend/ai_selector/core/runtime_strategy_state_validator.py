class RuntimeStrategyStateValidator:

    def validate(self, state):

        weights = [
            value
            for key, value in state.items()
            if key.endswith("_weight")
        ]

        if any(
            w < 0 or w > 1
            for w in weights
        ):
            return {
                "valid": False,
                "reason": "weight_out_of_range"
            }

        return {
            "valid": True,
            "state": state
        }