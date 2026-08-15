"""
Feedback Collector

Stage54:
Feedback Learning Integration
"""

from .schema import FeedbackRecord
from .storage import FeedbackStorage


class FeedbackCollector:


    def __init__(self, storage=None):

        self.storage = (
            storage
            if storage
            else FeedbackStorage()
        )


    def collect(
        self,
        stock_code,
        prediction,
        actual_result="",
        score=0.0,
        source="unknown",
        metadata=None
    ):
        """
        收集一条反馈
        """

        record = FeedbackRecord(
            stock_code=stock_code,
            prediction=prediction,
            actual_result=actual_result,
            score=score,
            source=source,
            metadata=metadata or {}
        )


        self.storage.save(
            record.to_dict()
        )


        return record