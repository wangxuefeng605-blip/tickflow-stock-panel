"""
Runtime Recovery Manager

Stage23 Production Reliability
"""


class RecoveryManager:

    def __init__(self, max_retry=3):

        self.max_retry = max_retry


    def execute(
        self,
        func,
        fallback=None
    ):

        last_error = None


        for _ in range(self.max_retry):

            try:

                return func()


            except Exception as e:

                last_error = e


        return fallback


    def retry_count(self):

        return self.max_retry