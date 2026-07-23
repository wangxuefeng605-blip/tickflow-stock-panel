import requests


# Telegram机器人Token
BOT_TOKEN = "8465185113:AAFdwqIIjnF2xoME91gWNZu00FhNp2gYPGg"


# Telegram聊天ID
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
        data=data,
        timeout=20
    )


    print(response.json())


    return response.json()