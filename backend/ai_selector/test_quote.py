import os

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("ALL_PROXY", None)

import akshare as ak


df = ak.stock_zh_a_daily(
    symbol="sz000001",
    adjust="qfq"
)


print(df.head())

print(df.tail())