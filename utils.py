import dialogflow_v2 as dialogflow
import logging
import os
PROJECT_ID = os.environ['PROJECT_ID']
TELEGRAM_USER_CHAT_ID = os.environ['TELEGRAM_USER_CHAT_ID']


def get_reply_from_dialog_flow(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, TELEGRAM_USER_CHAT_ID)
    text_input = dialogflow.types.TextInput(text=text, language_code="RU")
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)
