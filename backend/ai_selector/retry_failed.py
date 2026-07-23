import pandas as pd

from fast_scanner import run_fast_scan


df=pd.read_csv(
    "scan_failed.csv",
    dtype={"code":str}
)


codes=df.code.tolist()


print(
    "重新扫描:",
    len(codes)
)


run_fast_scan(
    codes
)
