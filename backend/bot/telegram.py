import requests


BOT_TOKEN = "8465185113:AAFdwqIIjnF2xoME91gWNZu00FhNp2gYPGg"

CHAT_ID = "7305956367"


def send_message(text):

    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": CHAT_ID,
        "text": text
    }

    response = requests.post(
        url,
        data=data
    )

    return response.json()



if __name__ == "__main__":

    msg = """
AI股票机器人测试

今天Top10:
1. 测试股票
2. 测试股票
3. 测试股票

系统运行正常
"""

    result = send_message(msg)

    print(result)