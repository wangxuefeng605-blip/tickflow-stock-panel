import time


class MarketScheduler:


    def __init__(
        self,
        interval=300
    ):

        self.interval = interval



    def wait(self):

        time.sleep(
            self.interval
        )