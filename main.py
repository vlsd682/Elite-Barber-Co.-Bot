import telebot
from config import Config
from main_menu import MainMenuHandler
from feedback import FeedbacksHandler, ViewFeedbackHandler, AddFeedbackHandler, DeleteFeedbackHandler
from navigation import CommandHistory, BackHandler

class Bot:
    '''
    Class for managing a Telegram bot.

    Attributes:
    telegram_bot -- TeleBot instance for interaction with Telegram API
    main_menu -- MainMenu instance for processing bot commands
    feedback_handler -- FeedbacksHandler instance for managing feedback-related commands
    view_feedback_handler -- ViewFeedbackHandler instance for viewing feedbacks
    add_feedback_handler -- AddFeedbackHandler instance for adding feedbacks
    delete_feedback_handler -- DeleteFeedbackHandler instance for deleting feedbacks
    '''
    def __init__(self):
        '''Create TeleBot instance with a token and initializes MainMenu.'''
        self.telegram_bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)
        self.CommandHistory = CommandHistory()
        self.BackHandler = BackHandler(self)
        self.MainMenuHandler = MainMenuHandler(self)
        self.FeedbacksHandler = FeedbacksHandler(self)
        self.ViewFeedbackHandler = ViewFeedbackHandler(self)
        self.AddFeedbackHandler = AddFeedbackHandler(self)
        self.DeleteFeedbackHandler = DeleteFeedbackHandler(self)
        self.register_handlers()

    def register_handlers(self):
        '''Register all command handlers.'''
        self.BackHandler.back_bnt_handler()
        self.MainMenuHandler.start_bnt_handler()
        self.MainMenuHandler.conditions_btn_handler()
        self.MainMenuHandler.help_btn_handler()
        self.FeedbacksHandler.feedbacks_btn_handler()
        self.ViewFeedbackHandler.view_feedback_bnt_handler()
        self.AddFeedbackHandler.add_feedback_btn_handler()
        self.DeleteFeedbackHandler.delete_feedback_bnt_handler()

    def send_message(self, chat_id, text, buttons=None, parse_mode = 'Markdown'):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        if buttons:
            arranged_buttons = self.arrange_buttons(chat_id, buttons)
            for row in arranged_buttons[chat_id]:
                markup.add(*row)
        self.telegram_bot.send_message(chat_id, text, reply_markup=markup, parse_mode=parse_mode)

    def arrange_buttons(self, chat_id, buttons):
        arranged_buttons = {chat_id: []}
        current_row = []
        current_row_length = 0
        for word in buttons:
            word_length = len(word)
            if current_row_length + word_length + len(current_row) > 25:
                arranged_buttons[chat_id].append(current_row)
                current_row = []
                current_row_length = 0
            current_row.append(word)
            current_row_length += word_length
        if current_row:
            arranged_buttons[chat_id].append(current_row)
        return arranged_buttons

    def start_bot(self):
        self.telegram_bot.polling()


def main():
    bot = Bot()
    bot.start_bot()

if __name__ == '__main__':
    main()
