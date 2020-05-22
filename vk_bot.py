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
    vk_key = os.environ['VK_KEY']
    project_id = os.environ['PROJECT_ID']
    telegram_user_chat_id = os.environ['TELEGRAM_USER_CHAT_ID']
    notification_telegram_token = os.environ['NOTIFICATION_TELEGRAM_TOKEN']
    notification_bot = telebot.TeleBot(notification_telegram_token)
    logger.setLevel(logging.WARNING)
    logger.addHandler(TelegramLogsHandler(notification_bot, telegram_user_chat_id))
    vk_session = vk_api.VkApi(token=vk_key)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        try:
           if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                vk_session_id = 'vk_'+ event.user_id
                vk_user_id = event.user_id
                response = get_reply_from_dialog_flow(event.text,project_id, vk_session_id)
                if not response.query_result.intent.is_fallback:
                    vk_api.messages.send(user_id=vk_user_id,message=response,random_id=random.randint(1, 1000))
        except Exception as error_msg:
            logger.error('VK bot is broken by error: {}'.format(error_msg))


if __name__ == '__main__':
    main()