import os


os.environ.pop(
    "HTTP_PROXY",
    None
)

os.environ.pop(
    "HTTPS_PROXY",
    None
)

os.environ.pop(
    "ALL_PROXY",
    None
)


import akshare as ak



def test_quote():

    df = ak.stock_zh_a_daily(
        symbol="sz000001",
        adjust="qfq"
    )


    assert df is not None

    assert len(df) > 0