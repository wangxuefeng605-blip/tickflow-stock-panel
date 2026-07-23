"""
Scanner V3 Data Types

统一数据模型，供：
- task_queue.py
- worker.py
- worker_pool.py
- engine.py
- writer.py
- progress.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any


# ===========================
# Scanner Status
# ===========================

class ScannerStatus(Enum):
    IDLE = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()
    STOPPED = auto()
    COMPLETED = auto()
    FAILED = auto()


# ===========================
# Task Priority
# ===========================

class TaskPriority(Enum):
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


# ===========================
# Scan Task
# ===========================

@dataclass(slots=True)
class ScanTask:
    code: str
    priority: TaskPriority = TaskPriority.NORMAL
    retry_count: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


# ===========================
# Scan Result
# ===========================

@dataclass(slots=True)
class ScanResult:
    code: str
    alpha_score: float = 0.0

    factors: dict[str, float] = field(default_factory=dict)

    success: bool = True

    error: str | None = None

    elapsed: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        """
        与当前 CSV Writer 保持兼容
        """

        return {
            "code": self.code,
            "alpha_score": self.alpha_score,
            **self.factors,
        }


# ===========================
# Retry Task
# ===========================

@dataclass(slots=True)
class RetryTask:
    task: ScanTask
    last_error: str
    retry_count: int = 0


# ===========================
# Worker State
# ===========================

@dataclass(slots=True)
class WorkerInfo:
    worker_id: int

    current_code: str | None = None

    processed: int = 0

    success: int = 0

    failed: int = 0


# ===========================
# Metrics
# ===========================

@dataclass(slots=True)
class ScanMetrics:

    total: int = 0

    pending: int = 0

    running: int = 0

    completed: int = 0

    failed: int = 0

    retry: int = 0


# ===========================
# Progress Snapshot
# ===========================

@dataclass(slots=True)
class ProgressSnapshot:

    success: int = 0

    failed: int = 0

    speed: float = 0.0

    eta: float = 0.0

    elapsed: float = 0.0