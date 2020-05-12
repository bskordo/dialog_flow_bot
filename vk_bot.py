import random
import vk_api
import logging
import telebot
import os
from utils import TelegramLogsHandler
from utils import get_reply_from_dialog_flow
from vk_api.longpoll import VkLongPoll, VkEventType


NOTIFICATION_TELEGRAM_TOKEN = os.environ['NOTIFICATION_TELEGRAM_TOKEN']
TELEGRAM_USER_CHAT_ID =os.environ['TELEGRAM_USER_CHAT_ID']
VK_KEY = os.environ['VK_KEY']
logger = logging.getLogger('Logger')


def reply_to_user(event, vk_api, text):
    try:
        vk_api.messages.send(
            user_id=event.user_id,
            message=text,
            random_id=random.randint(1, 1000))
    except Exception as error_msg:
            logger.error('Message can not send because of error: {}'.format(error_msg))


def main():
    notification_bot = telebot.TeleBot(NOTIFICATION_TELEGRAM_TOKEN)
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramLogsHandler(notification_bot, TELEGRAM_USER_CHAT_ID))
    vk_session = vk_api.VkApi(token=VK_KEY)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        try:
           if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                vk_session_id = event.user_id
                response = get_reply_from_dialog_flow(event.text, vk_session_id)
                if not response.query_result.intent.is_fallback:
                    vk_api.messages.send(user_id=vk_session_id,message=response,random_id=random.randint(1, 1000))
        except Exception as error_msg:
            logger.error('VK bot is broken by error: {}'.format(error_msg))


if __name__ == '__main__':
    main()