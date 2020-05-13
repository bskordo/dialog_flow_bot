import random
import vk_api
import logging
import telebot
import os
from utils import TelegramLogsHandler
from utils import get_reply_from_dialog_flow
from vk_api.longpoll import VkLongPoll, VkEventType


logger = logging.getLogger('Logger')


def main():
    vk_key = os.environ['vk_key']
    telegram_user_chat_id = os.environ['telegram_user_chat_id']
    notification_telegram_token = os.environ['notification_telegram_token']
    notification_bot = telebot.TeleBot(notification_telegram_token)
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramLogsHandler(notification_bot, telegram_user_chat_id))
    vk_session = vk_api.VkApi(token=vk_key)
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