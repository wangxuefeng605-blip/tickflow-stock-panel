"""
Feedback Storage Layer

Stage54:
Feedback Learning Integration

负责：
- 保存用户/系统反馈
- 读取历史反馈
- 提供给 evaluator / learner 使用
"""


import json
from pathlib import Path
from datetime import datetime, UTC


class FeedbackStorage:

    def __init__(self, path=None):

        if path is None:
            path = (
                Path(__file__)
                .resolve()
                .parents[2]
                / "data"
                / "feedback"
                / "feedback.json"
            )

        self.path = Path(path)

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(self, record):
        """
        保存一条反馈记录
        """

        records = self.load()

        record = dict(record)

        record.setdefault(
            "timestamp",
            datetime.now(UTC).isoformat()
        )

        records.append(record)

        self.path.write_text(
            json.dumps(
                records,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )


    def load(self):
        """
        加载全部反馈
        """

        if not self.path.exists():
            return []

        try:
            return json.loads(
                self.path.read_text(
                    encoding="utf-8"
                )
            )

        except Exception:
            return []


    def clear(self):
        """
        清空反馈
        """

        if self.path.exists():
            self.path.unlink()