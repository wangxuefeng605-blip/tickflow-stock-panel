class ScannerLearningIntegration:


    def __init__(self):

        self.learning_applied = False



    def apply(
        self,
        factors,
        learning_state
    ):

        result = factors.copy()

        weights = learning_state.get(
            "weights",
            {}
        )


        for key, value in result.items():

            if key in weights:

                result[key] = (
                    value *
                    weights[key]
                )


        return {
            **result,
            "learning_applied": True
        }



    def process(
        self,
        scanner_result,
        learning_state=None
    ):

        return self.apply(
            scanner_result,
            learning_state or {}
        )