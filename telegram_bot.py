import logging
import telebot
from utils import TelegramLogsHandler
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from utils import get_reply_from_dialog_flow

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_USER_CHAT_ID = os.environ['TELEGRAM_USER_CHAT_ID']
NOTIFICATION_TELEGRAM_TOKEN = os.environ['NOTIFICATION_TELEGRAM_TOKEN']
notification_bot = telebot.TeleBot(NOTIFICATION_TELEGRAM_TOKEN)
logger = logging.getLogger('Logger')


def reply_to_user(bot, update):
    msg_from_google = get_reply_from_dialog_flow(update.message.text)
    update.message.reply_text(msg_from_google.query_result.fulfillment_text)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
    logger.addHandler(TelegramLogsHandler(notification_bot, TELEGRAM_USER_CHAT_ID))


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text, reply_to_user))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramLogsHandler(notification_bot, TELEGRAM_USER_CHAT_ID))
    main()
