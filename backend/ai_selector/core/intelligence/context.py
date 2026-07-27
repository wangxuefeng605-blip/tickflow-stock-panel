from dataclasses import dataclass, field


@dataclass
class AIContext:

    # 当前市场状态
    market_state: str

    # 当前动态权重
    weights: dict = field(
        default_factory=dict
    )

    # 市场置信度
    confidence: float = 1.0


    def summary(self):

        return {
            "market_state": self.market_state,
            "weights": self.weights,
            "confidence": self.confidence
        }