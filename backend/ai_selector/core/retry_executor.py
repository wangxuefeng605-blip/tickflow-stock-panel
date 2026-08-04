from core.retry_manager import RetryManager


class RetryExecutor:

    def __init__(self):
        self.retry_manager = RetryManager()


    def run_retry(self):

        failed = self.retry_manager.get_failed()

        return {
            "retry_count": len(failed),
            "retry_completed": True,
            "failed_tasks": failed
        }