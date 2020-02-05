import io
import traceback
from tg_base_bot import BaseBot


class AdminBot(BaseBot):
    def __init__(self, token, chat_id):
        super().__init__(token)
        self.admin_chat_id = chat_id

    def log(self, app, message):
        message = message.replace('<', '&lt;').replace('>', '&gt;')
        text = '<b>[{}]</b> {}'.format(app.upper(), message)
        self.send_message(self.admin_chat_id, text, parse_mode='HTML')

    def log_error(self, app, exc_info):
        buf = io.StringIO('An exception occurred:\n')
        traceback.print_exception(*exc_info, file=buf)
        self.log(app, buf.getvalue())
