from telegram import Bot


TOKEN="你的TOKEN"

CHAT_ID="你的ID"


bot=Bot(
    token=TOKEN
)


def send_message(text):

    bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )