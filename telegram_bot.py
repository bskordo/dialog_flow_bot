import logging
import telebot
from utils import TelegramLogsHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import get_reply_from_dialog_flow
import os


PROJECT_ID = os.environ['PROJECT_ID']
logger = logging.getLogger('Logger')


def reply_to_user(bot, update):
    tg_chat_id = 'tg_'+ str(update.message.from_user.id)
    msg_from_google = get_reply_from_dialog_flow(update.message.text,PROJECT_ID, tg_chat_id)
    update.message.reply_text(msg_from_google.query_result.fulfillment_text)



def main():
    telegram_user_chat_id = os.environ['TELEGRAM_USER_CHAT_ID']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    notification_telegram_token = os.environ['NOTIFICATION_TELEGRAM_TOKEN']
    notification_bot = telebot.TeleBot(notification_telegram_token)
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramLogsHandler(notification_bot, telegram_user_chat_id))
    updater = Updater(telegram_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text, reply_to_user))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()