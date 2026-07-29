from .context import AIContext
from .state_engine import MarketStateEngine
from .weight_engine import WeightEngine
from .confidence import calculate_confidence


class ContextBuilder:


    def __init__(self):

        self.state_engine = MarketStateEngine()

        self.weight_engine = WeightEngine()



    def build(
        self,
        market_data=None
    ):


        if market_data is None:

            market_data = {

                "trend": 1,

                "volatility": 0.18,

                "breadth": 0.6,

                "index_change": 0.5,

                "volume_ratio": 1.2

            }


        state = self.state_engine.detect(
            market_data
        )


        weights = self.weight_engine.get_weights(
            state
        )


        return AIContext(

            market_state=state,

            weights=weights,

            confidence=calculate_confidence(
                market_data
            )

        )