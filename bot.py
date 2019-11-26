from telegram.ext import Updater, MessageHandler, Filters
from pytube import YouTube

from yandex import sendToScreen
import config


def youtubeToVideoUrl(url):
    yt = YouTube(url).streams.first()
    return yt.url


def getVideoUrl(url):
    if "youtube" in url:
        return youtubeToVideoUrl(url)
    # Other services can be here
    return url


def extractUrl(message):
    return message.text # TODO: getting url by entities info


def message_recieved(bot, update):
    
    user_id = update.message.chat_id
    # TODO: get yandex configs based on user_id
    
    url = extractUrl(update.message)
    video_url = getVideoUrl(url)
    result = sendToScreen(video_url)

    print(result)

    bot.send_message(chat_id=update.message.chat_id, text=result)


updater = Updater(token=config.telegram_bot_token, request_kwargs=config.proxy)

message_handler = MessageHandler(Filters.all, message_recieved)
updater.dispatcher.add_handler(message_handler)

print("Start polling...")

updater.start_polling()
