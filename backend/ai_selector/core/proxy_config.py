"""
Proxy Manager
v17.2 Stable
"""

import os


def disable_proxy():

    proxy_keys = [
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",

        "http_proxy",
        "https_proxy",
        "all_proxy",
    ]


    removed = []


    for key in proxy_keys:

        if key in os.environ:

            removed.append(key)
            os.environ.pop(key)


    if removed:

        print(
            "已关闭代理:",
            removed
        )