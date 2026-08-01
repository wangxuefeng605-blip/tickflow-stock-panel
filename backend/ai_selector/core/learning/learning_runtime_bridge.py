from .prediction_store import PredictionStore
from .feedback import evaluate_prediction
from .adaptive_weight import AdaptiveWeightEngine
from .weight_provider import WeightProvider


class LearningRuntimeBridge:

    def __init__(self):
        self.store = PredictionStore()
        self.weight_engine = AdaptiveWeightEngine()
        self.provider = WeightProvider()


    def record_predictions(self, results):
        self.store.save(results)


    def process_feedback(
        self,
        factor,
        entry,
        future
    ):

        feedback = evaluate_prediction(
            entry,
            future
        )

        self.weight_engine.adjust(
            factor,
            feedback["return"]
        )

        self.provider.update(
            self.weight_engine.weights
        )

        return feedback