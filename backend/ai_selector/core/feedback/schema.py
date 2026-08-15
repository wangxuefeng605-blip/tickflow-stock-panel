"""
Feedback Schema

Stage54:
Feedback Learning Integration

统一反馈数据结构
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class FeedbackRecord:
    """
    单条反馈记录
    """

    stock_code: str

    prediction: str

    actual_result: str = ""

    score: float = 0.0

    source: str = "unknown"

    metadata: dict = field(
        default_factory=dict
    )

    timestamp: str = field(
        default_factory=lambda:
            datetime.now(UTC).isoformat()
    )


    def to_dict(self):
        """
        转换为 Storage 可保存格式
        """

        return {
            "stock_code": self.stock_code,
            "prediction": self.prediction,
            "actual_result": self.actual_result,
            "score": self.score,
            "source": self.source,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }


    @classmethod
    def from_dict(cls, data):
        """
        从 Storage 数据恢复
        """

        return cls(
            stock_code=data.get(
                "stock_code",
                ""
            ),

            prediction=data.get(
                "prediction",
                ""
            ),

            actual_result=data.get(
                "actual_result",
                ""
            ),

            score=data.get(
                "score",
                0.0
            ),

            source=data.get(
                "source",
                "unknown"
            ),

            metadata=data.get(
                "metadata",
                {}
            ),

            timestamp=data.get(
                "timestamp",
                datetime.now(UTC).isoformat()
            )
        )