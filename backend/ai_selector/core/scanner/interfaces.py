"""
Scanner V3 - Core interfaces

定义扫描器核心接口（Contract Layer）
后续所有实现都必须遵循这些接口。
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable, Optional, Any

from .types import ScanTask, ScanResult, ScanStatistics


# ============================================================
# Queue
# ============================================================

class ITaskQueue(ABC):
    """任务队列接口"""

    @abstractmethod
    def put(self, task: ScanTask) -> None:
        """提交任务"""
        raise NotImplementedError

    @abstractmethod
    def put_many(self, tasks: Iterable[ScanTask]) -> None:
        """批量提交任务"""
        raise NotImplementedError

    @abstractmethod
    def get(self, timeout: Optional[float] = None) -> ScanTask:
        """获取任务"""
        raise NotImplementedError

    @abstractmethod
    def task_done(self) -> None:
        """标记任务完成"""
        raise NotImplementedError

    @abstractmethod
    def join(self) -> None:
        """等待所有任务完成"""
        raise NotImplementedError

    @abstractmethod
    def empty(self) -> bool:
        """队列是否为空"""
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        """关闭队列"""
        raise NotImplementedError


# ============================================================
# Worker
# ============================================================

class IWorker(ABC):
    """Worker 接口"""

    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def join(self, timeout: Optional[float] = None) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_running(self) -> bool:
        raise NotImplementedError


# ============================================================
# Worker Pool
# ============================================================

class IWorkerPool(ABC):
    """Worker 池接口"""

    @abstractmethod
    def start(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def shutdown(self, wait: bool = True) -> None:
        raise NotImplementedError

    @abstractmethod
    def resize(self, workers: int) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def worker_count(self) -> int:
        raise NotImplementedError


# ============================================================
# Writer
# ============================================================

class IWriter(ABC):
    """结果写入接口"""

    @abstractmethod
    def write(self, result: ScanResult) -> None:
        raise NotImplementedError

    @abstractmethod
    def write_many(self, results: Iterable[ScanResult]) -> None:
        raise NotImplementedError

    @abstractmethod
    def flush(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError


# ============================================================
# Progress
# ============================================================

class IProgress(ABC):
    """进度跟踪接口"""

    @abstractmethod
    def on_task_submitted(self, count: int = 1) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_task_completed(self, success: bool, elapsed: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def snapshot(self) -> ScanStatistics:
        raise NotImplementedError

    @abstractmethod
    def finish(self) -> None:
        raise NotImplementedError


# ============================================================
# Metrics
# ============================================================

class IMetrics(ABC):
    """性能指标接口"""

    @abstractmethod
    def record(self, name: str, value: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def increment(self, name: str, value: int = 1) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, name: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def summary(self) -> dict:
        raise NotImplementedError


# ============================================================
# Checkpoint
# ============================================================

class ICheckpointStore(ABC):
    """断点存储接口"""

    @abstractmethod
    def save(self, task: ScanTask) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self) -> Iterable[ScanTask]:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError


# ============================================================
# Retry
# ============================================================

class IRetryPolicy(ABC):
    """重试策略接口"""

    @abstractmethod
    def should_retry(self, task: ScanTask, exc: Exception) -> bool:
        raise NotImplementedError

    @abstractmethod
    def next_delay(self, retry_count: int) -> float:
        raise NotImplementedError