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


    proxies = {

        "http":
        "http://127.0.0.1:10809",

        "https":
        "http://127.0.0.1:10809"

    }


    response = requests.post(

        url,

        data=data,

        proxies=proxies,

        timeout=30

    )


    return response.json()



if __name__=="__main__":

    print(
        send_message(
            "AI股票机器人测试成功"
        )
    )