import akshare.utils.request as req


_old = req.requests.Session


class FixedSession(_old):

    def __init__(self):
        super().__init__()

        self.trust_env = False

        self.headers.update(
            {
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",

                "Referer":
                "https://quote.eastmoney.com/"
            }
        )


req.requests.Session = FixedSession