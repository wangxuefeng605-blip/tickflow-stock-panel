import os


os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"

os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"


print("代理已开启")