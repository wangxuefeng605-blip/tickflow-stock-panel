class RuntimeMetrics:


    def __init__(self):

        self.total_runs = 0

        self.success_runs = 0

        self.failed_runs = 0

        self.retry_count = 0

        self.recovery_success = 0



    def record_success(self):

        self.total_runs += 1

        self.success_runs += 1



    def record_failure(self):

        self.total_runs += 1

        self.failed_runs += 1



    def record_retry(self):

        self.retry_count += 1



    def record_recovery(self):

        self.recovery_success += 1



    def report(self):

        return {

            "total_runs": self.total_runs,

            "success_runs": self.success_runs,

            "failed_runs": self.failed_runs,

            "retry_count": self.retry_count,

            "recovery_success": self.recovery_success

        }