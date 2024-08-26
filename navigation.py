from collections import defaultdict, deque
import inspect


class CommandHistory:
    def __init__(self):
        self.COMMAND_HISTORY = defaultdict(deque)

    def update_command_history(self, user_id, command_name):
        self.COMMAND_HISTORY[user_id].append(command_name)
        print(self.COMMAND_HISTORY)

    def command_decorator(self, func):
        def wrapper(msg, *args, **kwargs):
            if self.last_command_the_same(msg.chat.id, func.__name__):
                pass
            else:
                self.update_command_history(msg.chat.id, func.__name__)
            return func(msg, *args, **kwargs)
        return wrapper

    def last_command_the_same(self, user_id, command_name):
        if len(self.COMMAND_HISTORY[user_id]) == 0:
            return False
        return command_name == self.COMMAND_HISTORY[user_id][-1]

    def execute_last_command(self, bot, user_id):
        print('back')


class BackHandler:
    def __init__(self, bot):
        self.bot = bot
        self.CommandHistory = bot.CommandHistory

    def back_bnt_handler(self):
        @self.bot.telegram_bot.message_handler(commands=['back'])
        @self.bot.telegram_bot.message_handler(func=lambda message: message.text == 'Назад')
        def back(msg):
            self.CommandHistory.execute_last_command(self, msg.chat.id)



