import os
import akshare as ak


class AkShareProvider:

    def get_market_data(self):

        http_proxy = os.environ.pop(
            "HTTP_PROXY",
            None
        )

        https_proxy = os.environ.pop(
            "HTTPS_PROXY",
            None
        )

        try:
            df = ak.stock_zh_a_spot_em()

            return df.to_dict(
                orient="records"
            )

        finally:

            if http_proxy:
                os.environ["HTTP_PROXY"] = http_proxy

            if https_proxy:
                os.environ["HTTPS_PROXY"] = https_proxy