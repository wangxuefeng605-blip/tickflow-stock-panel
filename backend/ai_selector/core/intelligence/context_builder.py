from .context import AIContext
from .state_engine import MarketStateEngine
from .weight_engine import WeightEngine


class ContextBuilder:


    def __init__(self):

        self.state_engine = (
            MarketStateEngine()
        )

        self.weight_engine = (
            WeightEngine()
        )


    def build(
        self,
        market_data
    ):


        state = (
            self.state_engine.detect(
                market_data
            )
        )


        weights = (
            self.weight_engine.get_weights(
                state
            )
        )


        return AIContext(
            market_state=state,
            weights=weights
        )