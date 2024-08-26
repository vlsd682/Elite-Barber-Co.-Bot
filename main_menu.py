from commands import StandardCommands, MainManuCommands, FeedbacksCommands, AppointmentCommands
from messages import MainMenuMessages


class MainMenuHandler:
    '''
    Class for handling basic commands: /start, /conditions, /help, /profile.

    Attributes:
    bot -- the instance used to interact with the Telegram API
    '''
    def __init__(self, bot):
        '''Initializes MainMenu with a bot instance.'''
        self.bot = bot
        self.CommandHistory = bot.CommandHistory
        self.MainMenuButtons = MainMenuButtons()

    def start_bnt_handler(self):
        @self.bot.telegram_bot.message_handler(commands=['start'])
        @self.bot.telegram_bot.message_handler(func=lambda message: message.text == 'Почати спочатку')
        @self.CommandHistory.command_decorator
        def start(msg):
            self.bot.send_message(msg.chat.id, MainMenuMessages.START_MSG, self.MainMenuButtons.start_btns(), parse_mode='HTML')

    def conditions_btn_handler(self):
        @self.bot.telegram_bot.message_handler(commands=['conditions'])
        @self.bot.telegram_bot.message_handler(func=lambda message: message.text == 'Умови')
        @self.CommandHistory.command_decorator
        def conditions(msg):
            self.bot.send_message(msg.chat.id, MainMenuMessages.CONDITIONS_MSG, self.MainMenuButtons.conditions_btns())


    def help_btn_handler(self):
        @self.bot.telegram_bot.message_handler(commands=['help'])
        @self.bot.telegram_bot.message_handler(func=lambda message: message.text == 'Допомога')
        @self.CommandHistory.command_decorator
        def help(msg):
            self.bot.send_message(msg.chat.id, MainMenuMessages.HELP_MSG, self.MainMenuButtons.help_btns())






class MainMenuButtons:
    '''
    Class for generating buttons for the main menu.
    '''
    def start_btns(self):
        return [
            StandardCommands.HELP_BTN,
            MainManuCommands.CONDITIONS_BTH,
            MainManuCommands.PROFILE_BNT,
            AppointmentCommands.APPOINTMENT_BNT,
            FeedbacksCommands.FEEDBACKS_BTN,
            StandardCommands.START_BTN,
            StandardCommands.BACK_BTN
        ]

    def conditions_btns(self):
        return [
            StandardCommands.HELP_BTN,
            MainManuCommands.PROFILE_BNT,
            AppointmentCommands.APPOINTMENT_BNT,
            FeedbacksCommands.FEEDBACKS_BTN,
            StandardCommands.START_BTN,
            StandardCommands.BACK_BTN
        ]

    def help_btns(self):
        return [
            MainManuCommands.PROFILE_BNT,
            MainManuCommands.CONDITIONS_BTH,
            AppointmentCommands.APPOINTMENT_BNT,
            FeedbacksCommands.FEEDBACKS_BTN,
            StandardCommands.START_BTN,
            StandardCommands.BACK_BTN
        ]